from meals.models import Guest, Invite, Meal, MealPart, Part
from rest_framework import serializers


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
