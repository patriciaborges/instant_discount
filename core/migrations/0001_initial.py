# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Business'
        db.create_table(u'core_business', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gps_latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=2)),
            ('gps_longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=2)),
            ('google_maps_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('paypal_account', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Business'])

        # Adding model 'Person'
        db.create_table(u'core_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('paypal_account', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Person'])

        # Adding model 'Offer'
        db.create_table(u'core_offer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('business', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Business'])),
            ('issued_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=13, decimal_places=2)),
            ('quantity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('quantity_available', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Offer'])

        # Adding model 'DoneDeal'
        db.create_table(u'core_donedeal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Person'])),
            ('offer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Offer'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('purchase_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('core', ['DoneDeal'])


    def backwards(self, orm):
        # Deleting model 'Business'
        db.delete_table(u'core_business')

        # Deleting model 'Person'
        db.delete_table(u'core_person')

        # Deleting model 'Offer'
        db.delete_table(u'core_offer')

        # Deleting model 'DoneDeal'
        db.delete_table(u'core_donedeal')


    models = {
        'core.business': {
            'Meta': {'object_name': 'Business'},
            'google_maps_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'purchase_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'core.offer': {
            'Meta': {'object_name': 'Offer'},
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