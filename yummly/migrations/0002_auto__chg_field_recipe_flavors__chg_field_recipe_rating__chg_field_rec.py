# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Recipe.flavors'
        db.alter_column('yummly_recipe', 'flavors', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipe.rating'
        db.alter_column('yummly_recipe', 'rating', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipe.name'
        db.alter_column('yummly_recipe', 'name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipe.remote_id'
        db.alter_column('yummly_recipe', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Recipe.source_display_name'
        db.alter_column('yummly_recipe', 'source_display_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Allergy.remote_id'
        db.alter_column('yummly_allergy', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Allergy.search_value'
        db.alter_column('yummly_allergy', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Allergy.description'
        db.alter_column('yummly_allergy', 'description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Cuisine.remote_id'
        db.alter_column('yummly_cuisine', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Cuisine.search_value'
        db.alter_column('yummly_cuisine', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Cuisine.description'
        db.alter_column('yummly_cuisine', 'description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Diet.remote_id'
        db.alter_column('yummly_diet', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Diet.search_value'
        db.alter_column('yummly_diet', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Diet.description'
        db.alter_column('yummly_diet', 'description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Ingredient.term'
        db.alter_column('yummly_ingredient', 'term', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Ingredient.remote_id'
        db.alter_column('yummly_ingredient', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Ingredient.search_value'
        db.alter_column('yummly_ingredient', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Ingredient.use_count'
        db.alter_column('yummly_ingredient', 'use_count', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Ingredient.ingredient_id'
        db.alter_column('yummly_ingredient', 'ingredient_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Course.remote_id'
        db.alter_column('yummly_course', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Course.search_value'
        db.alter_column('yummly_course', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Course.description'
        db.alter_column('yummly_course', 'description', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'Recipe.flavors'
        db.alter_column('yummly_recipe', 'flavors', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Recipe.rating'
        db.alter_column('yummly_recipe', 'rating', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Recipe.name'
        db.alter_column('yummly_recipe', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Recipe.remote_id'
        db.alter_column('yummly_recipe', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Recipe.source_display_name'
        db.alter_column('yummly_recipe', 'source_display_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Allergy.remote_id'
        db.alter_column('yummly_allergy', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Allergy.search_value'
        db.alter_column('yummly_allergy', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Allergy.description'
        db.alter_column('yummly_allergy', 'description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Cuisine.remote_id'
        db.alter_column('yummly_cuisine', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Cuisine.search_value'
        db.alter_column('yummly_cuisine', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Cuisine.description'
        db.alter_column('yummly_cuisine', 'description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Diet.remote_id'
        db.alter_column('yummly_diet', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Diet.search_value'
        db.alter_column('yummly_diet', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Diet.description'
        db.alter_column('yummly_diet', 'description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Ingredient.term'
        db.alter_column('yummly_ingredient', 'term', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Ingredient.remote_id'
        db.alter_column('yummly_ingredient', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Ingredient.search_value'
        db.alter_column('yummly_ingredient', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Ingredient.use_count'
        db.alter_column('yummly_ingredient', 'use_count', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Ingredient.ingredient_id'
        db.alter_column('yummly_ingredient', 'ingredient_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Course.remote_id'
        db.alter_column('yummly_course', 'remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Course.search_value'
        db.alter_column('yummly_course', 'search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Course.description'
        db.alter_column('yummly_course', 'description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    models = {
        'yummly.allergy': {
            'Meta': {'object_name': 'Allergy'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'yummly.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'yummly.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'yummly.diet': {
            'Meta': {'object_name': 'Diet'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'yummly.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'use_count': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'yummly.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['yummly.Course']", 'null': 'True', 'blank': 'True'}),
            'flavors': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['yummly.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'large_image_urls': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'small_image_urls': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'source_display_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'total_time_in_seconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yummly']