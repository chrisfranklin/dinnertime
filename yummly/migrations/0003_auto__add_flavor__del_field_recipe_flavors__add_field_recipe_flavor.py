# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Flavor'
        db.create_table('yummly_flavor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bitter', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('meaty', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('piquant', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('salty', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('sour', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
            ('sweet', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=20)),
        ))
        db.send_create_signal('yummly', ['Flavor'])

        # Deleting field 'Recipe.flavors'
        db.delete_column('yummly_recipe', 'flavors')

        # Adding field 'Recipe.flavor'
        db.add_column('yummly_recipe', 'flavor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['yummly.Flavor'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Flavor'
        db.delete_table('yummly_flavor')

        # Adding field 'Recipe.flavors'
        db.add_column('yummly_recipe', 'flavors',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Recipe.flavor'
        db.delete_column('yummly_recipe', 'flavor_id')


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
        'yummly.flavor': {
            'Meta': {'object_name': 'Flavor'},
            'bitter': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meaty': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'piquant': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'salty': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'sour': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'}),
            'sweet': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '20'})
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
            'flavor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['yummly.Flavor']", 'null': 'True', 'blank': 'True'}),
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