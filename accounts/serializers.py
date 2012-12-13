from accounts.models import UserProfile, UserContact
from rest_framework import serializers

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user',)

class UserContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserContact
        fields = ('owner', 'name', 'user', 'email')