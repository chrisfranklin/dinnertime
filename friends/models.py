import logging
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_delete, post_save, m2m_changed
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from friends.utils import get_datetime_now
from friends.managers import FriendshipManager, FriendshipInvitationManager, BlockingManager
from friends import settings as friends_settings


class Friendship(models.Model):
    """
    A friendship is a bi-directional association between two users who
    have both agreed to the association.
    """

    from_user = models.ForeignKey(User, verbose_name=_("from user"), related_name="_unused_")
    to_user = models.ForeignKey(User, verbose_name=_("to user"), related_name="friends")
    added = models.DateTimeField(_("added"), default=get_datetime_now)

    objects = FriendshipManager()

    class Meta:
        unique_together = [("to_user", "from_user")]
    
    def __unicode__(self):
        return "%s and %s" % (self.to_user, self.from_user)


class Blocking(models.Model):
    """
    A blocking is used to block user from sending invitations to another user
    (to protect from invitation spamming).
    """

    from_user = models.ForeignKey(User, verbose_name=_("from user"), related_name="blocking")
    to_user = models.ForeignKey(User, verbose_name=_("to user"), related_name="blocked_by")
    added = models.DateTimeField(_("added"), default=get_datetime_now)

    objects = BlockingManager()


class FriendshipInvitation(models.Model):
    """
    A friendship invite is an invitation from one user to another to be
    associated as friends.
    """

    from_user = models.ForeignKey(User, verbose_name=_("from user"), related_name="invitations_from")
    to_user = models.ForeignKey(User, verbose_name=_("to user"), related_name="invitations_to")
    message = models.TextField(_("message"))
    sent = models.DateTimeField(_("sent"), default=get_datetime_now)

    objects = FriendshipInvitationManager()

    def accept(self):
        if not Friendship.objects.are_friends(self.to_user, self.from_user):
            friendship = Friendship(to_user=self.to_user, from_user=self.from_user)
            friendship.save()
        self.delete()
        if "friends.contrib.suggestions" in settings.INSTALLED_APPS:
            from friends.contrib.suggestions.models import FriendshipSuggestion
            FriendshipSuggestion.objects.remove(self.to_user, self.from_user)

    def decline(self):
        self.delete()


class FriendListManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return super(FriendListManager, self).get_query_set(*args, **kwargs).filter(deleted=False)
    
    def deleted(self, *args, **kwargs):
        return super(FriendListManager, self).get_query_set(*args, **kwargs).filter(deleted=True)


class FriendList(models.Model):
    title = models.CharField(_("title"), max_length=100)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    owner = models.ForeignKey(User, related_name='lists')
    friends = models.ManyToManyField(User, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    
    objects = FriendListManager()
    
    def __unicode__(self):
        return "%s List: %s" % (self.owner, self.title)
    
    def delete(self, *args, **kwargs):
        if kwargs.get('force_delete', False):
            kwargs.pop('force_delete')
            super(FriendList).delete(*args, **kwargs)
        self.deleted = True
        self.save()
    

def only_add_friends(sender, instance, action, reverse, model, pk_set, *args, **kwargs):
    """
    Validates that a user is a friend before adding them to a FriendList.
    """
    friendlist = instance
    if action == 'pre_add' and not reverse and model == User:
        friends = User.objects.filter(pk__in=pk_set)
        for friend in friends:
            if not Friendship.objects.are_friends(friendlist.owner, friend):
                raise ValidationError("FriendList owner id %d is not friends with User id: %d" % (friendlist.id, friend.id))

m2m_changed.connect(only_add_friends, sender=FriendList.friends.through,
                    dispatch_uid='validate_adding_friends')


def remove_deleted_friendships_from_list(sender, instance, **kwargs):
    """
    When a friendship is deleted, remove each user from each other's lists.
    """
    user1 = instance.from_user
    user2 = instance.to_user
    
    for user, other_user in [(user1, user2), (user2, user1)]:
        lists = FriendList.objects.filter(owner=user)
        for l in lists:
                l.friends.remove(other_user)

pre_delete.connect(remove_deleted_friendships_from_list, sender=Friendship, dispatch_uid='friends_remove_deleted_friends_from_lists')


# signals receivers to send notifications

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

def send_invitation_sent_notification(sender, instance, created, **kwargs):
    if notification and created:
        notification.send([instance.to_user], "friends_invite", {"invitation": instance})
        notification.send([instance.from_user], "friends_invite_sent", {"invitation": instance})

def send_acceptance_sent_notification(sender, instance, created, **kwargs):
    if notification and created:
        notification.send([instance.to_user], "friends_accept_sent", {"from_user": instance.from_user})
        notification.send([instance.from_user], "friends_accept", {"to_user": instance.to_user})

def send_otherconnect_notification(sender, instance, created, **kwargs):
    if notification and created:
        for user in Friendship.objects.friends_for_user(instance.to_user):
            if user != instance.from_user:
                notification.send([user], "friends_otherconnect", {"your_friend": instance.to_user, "new_friend": instance.from_user})
        for user in Friendship.objects.friends_for_user(instance.from_user):
            if user != instance.to_user:
                notification.send([user], "friends_otherconnect", {"your_friend": instance.from_user, "new_friend": instance.to_user})

def send_friend_removed_notification(sender, instance, **kwargs):
    if notification:
        notification.send([instance.to_user], "friends_friend_removed", {"removed_friend": instance.from_user})
        notification.send([instance.from_user], "friends_friend_removed", {"removed_friend": instance.to_user})



if notification and friends_settings.FRIENDS_USE_NOTIFICATION_APP:

    post_save.connect(send_invitation_sent_notification, sender=FriendshipInvitation, dispatch_uid="friends_send_invitation_sent_notification")

    post_save.connect(send_acceptance_sent_notification, sender=Friendship, dispatch_uid="friends_send_acceptance_sent_notification")

    if friends_settings.NOTIFY_ABOUT_NEW_FRIENDS_OF_FRIEND:
        post_save.connect(send_otherconnect_notification, sender=Friendship, dispatch_uid="friends_send_otherconnect_notification")

    if friends_settings.NOTIFY_ABOUT_FRIENDS_REMOVAL:
        pre_delete.connect(send_friend_removed_notification, sender=Friendship, dispatch_uid="friends_send_friend_removed_notification")


