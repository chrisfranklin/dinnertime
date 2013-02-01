# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table('yummly_ingredient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ingredient_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('use_count', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Ingredient'])

        # Adding model 'Allergy'
        db.create_table('yummly_allergy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Allergy'])

        # Adding model 'Diet'
        db.create_table('yummly_diet', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Diet'])

        # Adding model 'Course'
        db.create_table('yummly_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Course'])

        # Adding model 'Cuisine'
        db.create_table('yummly_cuisine', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_value', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Cuisine'])

        # Adding model 'Recipe'
        db.create_table('yummly_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flavors', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('remote_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('small_image_urls', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('large_image_urls', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
            ('source_display_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('total_time_in_seconds', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('yummly', ['Recipe'])

        # Adding M2M table for field ingredients on 'Recipe'
        db.create_table('yummly_recipe_ingredients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['yummly.recipe'], null=False)),
            ('ingredient', models.ForeignKey(orm['yummly.ingredient'], null=False))
        ))
        db.create_unique('yummly_recipe_ingredients', ['recipe_id', 'ingredient_id'])

        # Adding M2M table for field course on 'Recipe'
        db.create_table('yummly_recipe_course', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('recipe', models.ForeignKey(orm['yummly.recipe'], null=False)),
            ('course', models.ForeignKey(orm['yummly.course'], null=False))
        ))
        db.create_unique('yummly_recipe_course', ['recipe_id', 'course_id'])


    def backwards(self, orm):
        # Deleting model 'Ingredient'
        db.delete_table('yummly_ingredient')

        # Deleting model 'Allergy'
        db.delete_table('yummly_allergy')

        # Deleting model 'Diet'
        db.delete_table('yummly_diet')

        # Deleting model 'Course'
        db.delete_table('yummly_course')

        # Deleting model 'Cuisine'
        db.delete_table('yummly_cuisine')

        # Deleting model 'Recipe'
        db.delete_table('yummly_recipe')

        # Removing M2M table for field ingredients on 'Recipe'
        db.delete_table('yummly_recipe_ingredients')

        # Removing M2M table for field course on 'Recipe'
        db.delete_table('yummly_recipe_course')


    models = {
        'yummly.allergy': {
            'Meta': {'object_name': 'Allergy'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'yummly.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'yummly.cuisine': {
            'Meta': {'object_name': 'Cuisine'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'yummly.diet': {
            'Meta': {'object_name': 'Diet'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'yummly.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_value': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'use_count': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'yummly.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'course': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['yummly.Course']", 'null': 'True', 'blank': 'True'}),
            'flavors': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredients': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['yummly.Ingredient']", 'null': 'True', 'blank': 'True'}),
            'large_image_urls': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'remote_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'small_image_urls': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'source_display_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'total_time_in_seconds': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['yummly']