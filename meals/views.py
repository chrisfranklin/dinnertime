from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

from .models import Meal


def max_guests(request, meal_id, direction):
    meal_object = get_object_or_404(Meal, pk=meal_id)
    if request.user == meal_object.host:
        if direction == "increase":
            meal_object.increase_max_guest()
        elif direction == "decrease":
            meal_object.decrease_max_guest()
        else:
            return HttpResponse("Please enter a direction")
        return HttpResponseRedirect("/meal/%s/") % meal_id
    else:
        return HttpResponse("You are not the host of this meal")
