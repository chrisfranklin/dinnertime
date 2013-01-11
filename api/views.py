from meals.models import Guest, Invite, Meal, MealPart, Part
from api.serializers import GuestSerializer, InviteSerializer, MealSerializer, MealPartSerializer, PartSerializer
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
    return render_to_response("meals/index.html", {'bum': "bum"}, context_instance=RequestContext(request))


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'Meals': reverse('meal-list', request=request),
        'MealParts': reverse('mealpart-list', request=request),
        'Parts': reverse('part-list', request=request),
        'Guests': reverse('guest-list', request=request),
        'Invites': reverse('invite-list', request=request),
    })


## == MEALS ==


class MealList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Meals.
    """
    model = Meal
    serializer_class = MealSerializer


class MealDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Meal.
    """
    model = Meal
    serializer_class = MealSerializer


## == MEALPARTS ==


class MealPartList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of MealParts.
    """
    model = MealPart
    serializer_class = MealPartSerializer


class MealPartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single MealPart.
    """
    model = MealPart
    serializer_class = MealPartSerializer


## == MEALPARTS ==


class PartList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Parts.
    """
    model = Part
    serializer_class = PartSerializer


class PartDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Part.
    """
    model = Part
    serializer_class = PartSerializer


## == GUESTS ==


class GuestList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Parts.
    """
    model = Guest
    serializer_class = GuestSerializer


class GuestDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Part.
    """
    model = Guest
    serializer_class = GuestSerializer


## == INVITES ==


class InviteList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of Parts.
    """
    model = Invite
    serializer_class = InviteSerializer


class InviteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single Part.
    """
    model = Invite
    serializer_class = InviteSerializer
