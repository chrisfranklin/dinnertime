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


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ('id', 'part_type', 'name', 'description', 'unit')


class MealPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealPart
        #fields = ('id', 'part', 'meal', 'status', 'quantity', 'added_by', 'fulfilled_by')


class MealSerializer(serializers.ModelSerializer):
    #invites = serializers.HyperlinkedRelatedField()
    #guests = serializers.ManyPrimaryKeyRelatedField('guests')
    host_username = serializers.Field(source='host.username')
    host_email = serializers.Field(source='host.email')
    name = serializers.Field(source='get_name')

    class Meta:
        model = Meal
        include = [('parts', MealPart)]
        #fields = ('id', 'name', 'venue', 'suitable_for', 'description', 'when', 'host', 'host_username', 'guests', 'current_guests', 'max_guests', 'privacy', 'parts', 'recipe')


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = ('id', 'meal', 'secret', 'invitee', 'status', 'plusones', 'max_plusones', 'single_use', 'invited_by')
