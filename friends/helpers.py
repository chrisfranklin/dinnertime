from django.utils.translation import ugettext_lazy as _
from friends.models import Friendship, Blocking, FriendshipInvitation

def make_friends(from_user, to_user):
    """
    Provides a helper function to create a friendship between two users.
    """
    if not Friendship.objects.are_friends(from_user, to_user):
        if from_user != to_user:
            friendship = Friendship(from_user=from_user, to_user=to_user)
            friendship.save()
            return True
    else:
        return False

def invite(from_user, to_user):
    """
    Provides a helper function to send a friendship invitation from one friend to another.
    """
    if from_user == to_user:
        raise ValueError(_to_user(u"You can't request friendship with yourself."))
    if Friendship.objects.are_friends(from_user, to_user):
        raise  ValueError(_(u"You are already friends with %(username)s.") % {'username': to_user.username})
    blocking = Blocking.objects.filter(from_user=to_user, to_user=from_user)
    if blocking.count() > 0:
        raise ValueError(_(u"You can't invite %(username)s to friends.") % {'username': to_user.username})
    if FriendshipInvitation.objects.is_invited(from_user, to_user):
        raise ValueError(_(u"Already requested friendship with %(username)s.") % {'username': to_user.username})
    invitation = FriendshipInvitation(from_user=from_user, to_user=to_user)
    invitation.save()
    return True

