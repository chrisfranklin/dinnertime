from meals.models import Meal
from api.serializers import MealSerializer
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
    })


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
