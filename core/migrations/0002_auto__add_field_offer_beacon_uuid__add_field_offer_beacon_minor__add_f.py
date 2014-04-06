# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Offer.beacon_uuid'
        db.add_column(u'core_offer', 'beacon_uuid',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)

        # Adding field 'Offer.beacon_minor'
        db.add_column(u'core_offer', 'beacon_minor',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Offer.beacon_major'
        db.add_column(u'core_offer', 'beacon_major',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Offer.beacon_uuid'
        db.delete_column(u'core_offer', 'beacon_uuid')

        # Deleting field 'Offer.beacon_minor'
        db.delete_column(u'core_offer', 'beacon_minor')

        # Deleting field 'Offer.beacon_major'
        db.delete_column(u'core_offer', 'beacon_major')


    models = {
        'core.business': {
            'Meta': {'object_name': 'Business'},
            'google_maps_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'gps_latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '2'}),
            'gps_longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'paypal_account': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.donedeal': {
            'Meta': {'object_name': 'DoneDeal'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Offer']"}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Person']"}),
            'purchase_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'core.offer': {
            'Meta': {'object_name': 'Offer'},
            'beacon_major': ('django.db.models.fields.IntegerField', [], {}),
            'beacon_minor': ('django.db.models.fields.IntegerField', [], {}),
            'beacon_uuid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'business': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Business']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issued_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '13', 'decimal_places': '2'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'quantity_available': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.person': {
            'Meta': {'object_name': 'Person'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'paypal_account': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']