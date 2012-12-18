from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from friends.utils import get_datetime_now
from friends.contrib.suggestions.managers import FriendshipSuggestionManager


class FriendshipSuggestion(models.Model):
    """
    A friendship suggestion connects two users that can possibly know each other.
    Suggestions can be created by somehow comparing some of user profiles fields
    (like city or address) or by importing user contacts from external services
    and then comparing names and email of imported contacts with users.
    """

    from_user = models.ForeignKey(User, verbose_name=_("from user"), related_name="suggestions_from")
    to_user = models.ForeignKey(User, verbose_name=_("to user"), related_name="suggestions_to")
    added = models.DateTimeField(_("added"), default=get_datetime_now)

    objects = FriendshipSuggestionManager()

    class Meta:
        unique_together = [("to_user", "from_user")]
        db_table = 'friends_suggestions_friendshipsuggestion'


class ImportedContact(models.Model):
    """
    Contact imported from external service.
    """
    # user who imported this contact
    owner = models.ForeignKey(User, verbose_name=_("owner"), related_name="imported_contacts")

    name = models.CharField(_("name"), max_length=255, null=True, blank=True)
    # Facebook does not give emails of user friends so email can be blank and
    # matching should be done using only name
    email = models.EmailField(_("email"), null=True, blank=True, max_length=255)

    added = models.DateTimeField(_("added"), default=get_datetime_now)

    service_name = models.CharField(_("service name"), max_length=255, null=True, blank=True)
    service_ownerid = models.BigIntegerField(blank=True, null=True)
    service_id = models.BigIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # We should store the contact in user contacts for future use.
        from accounts.models import UserContact
        usercontact_object = UserContact.objects.get_or_create(owner=self.owner, name=self.name)
        if not usercontact_object[0].email:
            # We need to store an email, we may also need to update the email we have, decide order of preference.
            if self.email:
                # We have an email to store
                usercontact_object[0].email = self.email
                usercontact_object[0].save()
        super(ImportedContact, self).save(*args, **kwargs)  # Call the "real" save() method.

    @property
    def display_name(self):
        dname = ''
        if self.email:
            dname = self.email
        if dname and self.name:
            dname += " - "
        dname += self.name
        return dname

    def __unicode__(self):
        return _("%(display_name)s (%(owner)s's contact)") % {'display_name': self.display_name, 'owner': self.owner}

    class Meta:
        db_table = 'friends_suggestions_importedcontact'
