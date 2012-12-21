from django.core.management.base import BaseCommand  # CommandError
from yummly.models import Ingredient, Course, Cuisine, Allergy, Diet, Recipe
#from oauth_hook import OAuthHook
import requests
import json
from pprint import pprint


class Command(BaseCommand):
    args = '<meta_class>'
    help = 'Download meta data matching specified class from yummly.'

    def handle(self, *args, **options):
        ck = "9687047d"
        cs = "48703203011932335cfaf5fb57ef4f1a"

        client = requests.session()
        #response = client.get('http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s&q=quiche' % (ck, cs))

        if args != "ingredient":
            response = client.get('http://api.yummly.com/v1/api/metadata/ingredient?_app_id=%s&_app_key=%s' % (ck, cs))
            pprint(response.content)
            try:
                results = json.loads(response.content[26:-2])  # This is for ingredients
            except:
                self.stdout.write("Could not load ingredients json, out of options, goodbye.")
            pprint(results)
            for ingredient in results:
                ingredient_object = Ingredient.objects.get_or_create(remote_id=ingredient['id'])[0]
                if "ingredientId" in ingredient:
                    ingredient_object.ingredient_id = ingredient['ingredientId']
                if "searchValue" in ingredient:
                    ingredient_object.search_value = ingredient['searchValue']
                if "term" in ingredient:
                    ingredient_object.term = ingredient['term']
                if "useCount" in ingredient:
                    ingredient_object.use_count = ingredient['useCount']
                print ingredient_object.save()

        if args != "course":
            response = client.get('http://api.yummly.com/v1/api/metadata/course?_app_id=%s&_app_key=%s' % (ck, cs))
            pprint(response.content)
            try:
                results = json.loads(response.content[23:-2])  # This is for ingredients
            except:
                self.stdout.write("Could not load course json, out of options, goodbye.")
            pprint(results)
            for course in results:
                course_object = Course.objects.get_or_create(remote_id=course['id'])[0]
                if "searchValue" in course:
                    course_object.search_value = course['searchValue']
                if "description" in course:
                    course_object.description = course['description']
                course_object.save()

        if args != "cuisine":
            response = client.get('http://api.yummly.com/v1/api/metadata/cuisine?_app_id=%s&_app_key=%s' % (ck, cs))
            pprint(response.content)
            try:
                results = json.loads(response.content[23:-2])  # This is for ingredients
            except:
                self.stdout.write("Could not load cuisine json, out of options, goodbye.")
            pprint(results)
            for cuisine in results:
                cuisine_object = Cuisine.objects.get_or_create(remote_id=cuisine['id'])[0]
                if "searchValue" in cuisine:
                    cuisine_object.search_value = cuisine['searchValue']
                if "description" in cuisine:
                    cuisine_object.description = cuisine['description']
                cuisine_object.save()

        if args != "allergy":
            response = client.get('http://api.yummly.com/v1/api/metadata/allergy?_app_id=%s&_app_key=%s' % (ck, cs))
            pprint(response.content)
            try:
                results = json.loads(response.content[23:-2])  # This is for ingredients
            except:
                self.stdout.write("Could not load allergy json, out of options, goodbye.")
            pprint(results)
            for allergy in results:
                allergy_object = Allergy.objects.get_or_create(remote_id=allergy['id'])[0]
                if "searchValue" in allergy:
                    allergy_object.search_value = allergy['searchValue']
                if "longDescription" in allergy:
                    allergy_object.description = allergy['longDescription']
                allergy_object.save()

        if args != "diet":
            response = client.get('http://api.yummly.com/v1/api/metadata/diet?_app_id=%s&_app_key=%s' % (ck, cs))
            pprint(response.content)
            try:
                results = json.loads(response.content[20:-2])  # This is for ingredients
            except:
                self.stdout.write("Could not load diet json, out of options, goodbye.")
            pprint(results)
            for diet in results:
                diet_object = Diet.objects.get_or_create(remote_id=diet['id'])[0]
                if "searchValue" in diet:
                    diet_object.search_value = diet['searchValue']
                if "longDescription" in diet:
                    diet_object.description = diet['longDescription']
                diet_object.save()

        if args != "recipe":
            response = client.get('http://api.yummly.com/v1/api/recipes?_app_id=%s&_app_key=%s&q=quiche&maxResult=20' % (ck, cs))
            #pprint(response.content)
            try:
                results = json.loads(response.content)  # This is for ingredients
            except:
                self.stdout.write("Could not load recipe json, out of options, goodbye.")
            pprint(results)
            for recipe in results["matches"]:
                print recipe.keys()
                recipe_object = Recipe.objects.get_or_create(remote_id=recipe['id'])[0]
                if "attributes" in recipe:
                    for attribute in recipe["attributes"]:
                        print attribute
                        if "course" in recipe['attributes']:
                            print recipe['attributes']['course']
                            for course in recipe['attributes']['course']:
                                recipe_object.course.add(Course.objects.get(description=course))
                if "recipeName" in recipe:
                    recipe_object.name = recipe['recipeName']
                if "rating" in recipe:
                    recipe_object.rating = recipe['rating']
                if "smallImageUrls" in recipe:
                    recipe_object.small_image_urls = recipe['smallImageUrls']  # Add code for big images here
                    image_list = list()
                    for image in recipe['smallImageUrls']:
                        image_list.append(image[:-5] + "xl.png")
                    recipe_object.large_image_urls = image_list
                if "totalTimeInSeconds" in recipe:
                    recipe_object.total_time_in_seconds = recipe['totalTimeInSeconds']
                if "sourceDisplayName" in recipe:
                    recipe_object.source_display_name = recipe['sourceDisplayName']
                if "ingredients" in recipe:
                    recipe_object.ingredients.clear()
                    for ingredient in recipe['ingredients']:
                        recipe_object.ingredients.add(Ingredient.objects.get_or_create(term=ingredient)[0])
                recipe_object.save()

        # flavors = models.CharField(max_length=50, blank=True, null=True)
        # remote_id = models.CharField(max_length=50, blank=True, null=True)
        # ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)
        # rating = models.CharField(max_length=50, blank=True, null=True)
        # name = models.CharField(max_length=50, blank=True, null=True)
        # small_image_urls = JSONField(blank=True, null=True)
        # large_image_urls = JSONField(blank=True, null=True)
        # source_display_name = models.CharField(max_length=50, blank=True, null=True)
        # total_time_in_seconds = models.IntegerField(blank=True, null=True)
        # course = models.ForeignKey(Course, blank=True, null=True)  # get from attributes

        # else:
        #     raise CommandError("Only ingredient or course works for now. %s" % args)

        # for poll_id in args:
        #     try:
        #         poll = Poll.objects.get(pk=int(poll_id))
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)
