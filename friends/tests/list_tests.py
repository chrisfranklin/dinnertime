"""
The test fixture contains the following users:

In [8]: for u in User.objects.all(): print u.id, u.username
1 user1
2 user2
3 user3
4 user4
5 user5
6 user6
7 user7
8 user8
9 user9
10 user10

In [9]: for f in Friendship.objects.all(): print f.id, f.from_user, f.to_user
2 user1 user2
3 user1 user3
4 user1 user4
5 user5 user1
6 user6 user1
7 user7 user1

In [10]: for l in FriendList.objects.all(): print l.id, l.owner, l.friends.all()
1 user1 []

In [11]: for b in Blocking.objects.all(): print b.id, b.from_user, b.to_user
1 user10 user1

"""
from operator import attrgetter
from django.test import TestCase
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from friends.models import Friendship, FriendList


def sort_list(the_list, attr='id'):
    the_list.sort(key=attrgetter(attr))


class ListTestCase(TestCase):
    fixtures = ['friends_test_fixture.json']
    
    def setUp(self):
        self.user1 = User.objects.get(username='user1')
        self.user1_list = FriendList.objects.get(owner=self.user1)
    
    def test_can_add_friend(self):
        friend = User.objects.get(id=2)
        original_count = self.user1_list.friends.all().count()
        self.user1_list.friends.add(friend)
        new_count = self.user1_list.friends.all().count()
        self.assertTrue(friend in self.user1_list.friends.all())
        self.assertEquals(original_count + 1, new_count)
    
    def test_cannot_add_non_friends(self):
        non_friend = User.objects.get(id=8)
        self.assertRaises(ValidationError, self.user1_list.friends.add, non_friend)
    
    def test_remove_from_list_when_deleting_friendship(self):
        friend = User.objects.get(id=2)
        self.user1_list.friends.add(friend)
        friendship = Friendship.objects.get(id=2)
        friendship.delete()
        self.assertTrue(friend not in self.user1_list.friends.all())
        
        