from meals.models import Guest, Invite, Meal, MealPart, Part
from accounts.models import UserProfile, UserContact
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        field = ('id', 'user', 'first_name', 'last_name', 'diet', 'allergies', 'likes', 'dislikes')


class UserContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserContact
        fields = ('owner', 'name', 'user', 'email')


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'user', 'meal', 'invite')


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'venue', 'suitable_for', 'description', 'when', 'host', 'guests', 'current_guests', 'max_guests', 'privacy', 'parts', 'recipe')


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
