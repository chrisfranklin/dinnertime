from .models import Meal


## API STUFF BELOW

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from meals.serializers import MealSerializer


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
