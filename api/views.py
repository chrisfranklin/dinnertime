from meals.models import Guest, Invite, Meal, MealPart, Part
from accounts.models import UserProfile, UserContact
from api.serializers import GuestSerializer, InviteSerializer, MealSerializer, MealPartSerializer, PartSerializer, UserProfileSerializer, UserContactSerializer, UserSerializer
#from django.http import Http404
from rest_framework import generics
#from rest_framework.views import APIView
from rest_framework.decorators import api_view
#from rest_framework.decorators import api_view

from rest_framework.response import Response
#from rest_framework import status
from rest_framework.reverse import reverse

from django.shortcuts import render_to_response

from django.template import RequestContext


def index(request):
    """
    Serves embedded javascript MVC test page
    """
    return render_to_response("meals/index.html", {'test': "test"}, context_instance=RequestContext(request))


@api_view(['GET'])
def api_root(request, format=None):
    """
    Lists all available models in API and provides an entry point.
    """
    return Response({
        'Meals': reverse('meal-list', request=request),
        'MealParts': reverse('mealpart-list', request=request),
        'Parts': reverse('part-list', request=request),
        'Guests': reverse('guest-list', request=request),
        'Invites': reverse('invite-list', request=request),
        'UserProfiles': reverse('userprofile-list', request=request),
        'UserContacts': reverse('usercontact-list', request=request),
    })


## == MEALS ==
class MealList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of Meals.
    """
    model = Meal
    serializer_class = MealSerializer


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides an API endpoint that represents a single Meal.
    """
    model = Meal
    serializer_class = MealSerializer


## == MEALPARTS ==


class MealPartList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of MealParts.
    """
    model = MealPart
    serializer_class = MealPartSerializer


class MealPartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides an API endpoint that represents a single MealPart.
    """
    model = MealPart
    serializer_class = MealPartSerializer


## == MEALPARTS ==


class PartList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of Parts.
    """
    model = Part
    serializer_class = PartSerializer


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides an API endpoint that represents a single Part.
    """
    model = Part
    serializer_class = PartSerializer


## == GUESTS ==


class GuestList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of Parts.
    """
    model = Guest
    serializer_class = GuestSerializer


class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides an API endpoint that represents a single Part.
    """
    model = Guest
    serializer_class = GuestSerializer


## == INVITES ==


class InviteList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of Parts.
    """
    model = Invite
    serializer_class = InviteSerializer


class InviteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Provides an API endpoint that represents a single Part.
    """
    model = Invite
    serializer_class = InviteSerializer


## == USERS ==
from django.contrib.auth.models import User

class UserList(generics.ListCreateAPIView):
    """
    Provides an API endpoint that represents a list of Users.

    """
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single User.
    """
    model = User
    serializer_class = UserSerializer



## == USERPROFILES aka PROFILES} ==


class UserProfileList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Parts.
    """
    model = UserProfile
    serializer_class = UserProfileSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Part.
    """
    model = UserProfile
    serializer_class = UserProfileSerializer


## == USERCONTACTS aka CONTACTS} ==


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
