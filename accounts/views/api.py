from accounts.models import UserContact, UserProfile
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from accounts.serializers import UserContactSerializer, UserProfileSerializer

@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'UserContacts': reverse('UserContact-list', request=request),
        'UserProfiles': reverse('UserProfile-list', request=request),
    })

class UserContactList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of UserContacts.
    """
    model = UserContact
    serializer_class = UserContactSerializer

class UserContactDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single UserContact.
    """
    model = UserContact
    serializer_class = UserContactSerializer

class UserProfileList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of UserProfiles.
    """
    model = UserProfile
    serializer_class = UserProfileSerializer

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single UserProfile.
    """
    model = UserProfile
    serializer_class = UserProfileSerializer