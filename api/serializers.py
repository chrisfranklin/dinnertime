from meals.models import Guest, Invite, Meal, MealPart, Part
from accounts.models import UserProfile, UserContact
from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        field = ('id', 'user', 'first_name', 'last_name', 'diet', 'allergies', 'likes', 'dislikes')


class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = ('owner', 'name', 'user', 'email')


class UserSerializer(serializers.ModelSerializer):
    #snippets = serializers.ManyHyperlinkedRelatedField(view_name='snippet-detail')

    class Meta:
        model = User
        fields = ('url', 'username')


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'meal', 'invite')


class User(object):
    """
    A color represented in the RGB colorspace.
    """
    def __init__(self, uid, name, email=None):
        self.uid, self.name, self.email = uid, name, email


class UserField(serializers.WritableField):
    """
    Color objects are serialized into "rgb(#, #, #)" notation.
    """
    def to_native(self, obj):
        return "%d, %d, %d" % (obj.uid, obj.name, obj.email)

    def from_native(self, data):
        data = data.strip('rgb(').rstrip(')')
        uid, name, email = [int(col) for col in data.split(',')]
        return User(uid, name, email)


class MealSerializer(serializers.ModelSerializer):
    #invites = serializers.HyperlinkedRelatedField()
    #guests = serializers.ManyPrimaryKeyRelatedField('guests')
    host_username = serializers.Field(source='host.username')

    class Meta:
        model = Meal
        #fields = ('id', 'name', 'venue', 'suitable_for', 'description', 'when', 'host', 'host_username', 'guests', 'current_guests', 'max_guests', 'privacy', 'parts', 'recipe')


class MealPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealPart
        fields = ('id', 'part', 'meal', 'status', 'quantity', 'added_by', 'fulfilled_by')


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'part_type', 'name', 'description', 'unit')


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('id', 'meal', 'secret', 'invitee', 'status', 'plusones', 'max_plusones', 'single_use', 'invited_by')
