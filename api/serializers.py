from meals.models import Guest, Invite, Meal, MealPart, Part
from accounts.models import UserProfile, UserContact
from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes UserProfile objects for the API
    """
    class Meta:
        model = UserProfile
        field = ('id', 'user', 'first_name', 'last_name', 'diet', 'allergies', 'likes', 'dislikes')


class UserContactSerializer(serializers.ModelSerializer):
    """
    Serializes UserContact objects for the API
    """
    class Meta:
        model = UserContact
        fields = ('owner', 'name', 'user', 'email')


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes User objects for the API
    """
    #snippets = serializers.ManyHyperlinkedRelatedField(view_name='snippet-detail')

    class Meta:
        model = User
        fields = ('url', 'username')


class GuestSerializer(serializers.ModelSerializer):
    """
    Serializes Guest objects for the API
    """
    class Meta:
        model = Guest
        fields = ('id', 'meal', 'invite')


class PartSerializer(serializers.ModelSerializer):
    """
    Serializes Part objects for the API
    """
    class Meta:
        model = Part
        fields = ('id', 'part_type', 'name', 'description', 'unit')


class MealPartSerializer(serializers.ModelSerializer):
    """
    Serializes MealPart objects for the API
    """

    class Meta:
        model = MealPart
        #fields = ('id', 'part', 'meal', 'status', 'quantity', 'added_by', 'fulfilled_by')


class MealSerializer(serializers.ModelSerializer):
    """
    Serializes Meal objects for the API
    """
    #invites = serializers.HyperlinkedRelatedField()
    #guests = serializers.ManyPrimaryKeyRelatedField('guests')
    host_username = serializers.Field(source='host.username')
    host_email = serializers.Field(source='host.email')
    name = serializers.Field(source='get_name')
    past = serializers.Field(source='past')
    image = serializers.Field(source='get_image')
    small_image = serializers.Field(source='get_image_small')

    class Meta:
        model = Meal
        include = [('parts', MealPart)]
        #fields = ('id', 'name', 'venue', 'suitable_for', 'description', 'when', 'host', 'host_username', 'guests', 'current_guests', 'max_guests', 'privacy', 'parts', 'recipe')


class InviteSerializer(serializers.ModelSerializer):
    """
    Serializes Invite objects for the API
    """
    class Meta:
        model = Invite
        fields = ('id', 'meal', 'secret', 'invitee', 'status', 'plusones', 'max_plusones', 'single_use', 'invited_by')
