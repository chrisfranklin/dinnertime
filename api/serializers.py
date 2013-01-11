from meals.models import Meal
from rest_framework import serializers


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'name', 'venue', 'suitable_for', 'description',  'when', 'host', 'guests', 'current_guests',  'max_guests', 'privacy', 'parts', 'recipe')

