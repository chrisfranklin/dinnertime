from django.db import models
from django.db.models import Q


class FriendshipManager(models.Manager):
    """
    Provides an interface to friends 
    """

    def friends_for_user(self, user):
        """
        Returns friends for specific user
        """
        friends = []
        qs = self.filter(Q(from_user=user) | Q(to_user=user)).select_related(depth=1)
        for friendship in qs:
            if friendship.from_user == user:
                friends.append(friendship.to_user)
            else:
                friends.append(friendship.from_user)
        return friends

    def are_friends(self, user1, user2):
        """
        Returns boolean value of whether user1 and user2 are currently friends.
        """
        return self.filter(
            Q(from_user=user1, to_user=user2) |
            Q(from_user=user2, to_user=user1)
        ).count() > 0

    def remove(self, user1, user2):
        """
        Removes specific user from another specific users friends list.
        """
        friendships = self.filter(from_user=user1, to_user=user2)
        if not friendships:
            friendships = self.filter(from_user=user2, to_user=user1)
        if friendships:
            friendships.delete()


class FriendshipInvitationManager(models.Manager):
    """
    Provides an interface to friendship invitations
    """

    def is_invited(self, user1, user2):
        """
        Returns boolean value of whether user1 has been invited to a friendship by user2
        """
        return self.filter(
            Q(from_user=user1, to_user=user2) |
            Q(from_user=user2, to_user=user1)
        ).count() > 0

    def remove(self, user1, user2):
        """
        Removes friendship request from user1 to user2.
        """
        invitations = self.filter(from_user=user1, to_user=user2)
        if not invitations:
            invitations = self.filter(from_user=user2, to_user=user1)
        if invitations:
            invitations.delete()


class BlockingManager(models.Manager):
    """
    Provides an interface to blocked users for all users.
    """

    def blocked_for_user(self, user):
        """
        Returns users that have blocked the specified user.
        """
        blocked = []
        qs = self.filter(from_user=user).select_related(depth=1)
        for blocking in qs:
            blocked.append(blocking.to_user)
        return blocked

