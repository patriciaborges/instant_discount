# -*- coding: utf-8 -*-

from django.db import models
import datetime


class Business(models.Model):
	gps_latitude = models.DecimalField(max_digits=13, decimal_places=2)
	gps_longitude = models.DecimalField(max_digits=13, decimal_places=2)
	google_maps_url = models.CharField(max_length=255, blank=True)
	name = models.CharField(max_length=255)
	paypal_account = models.CharField(max_length=255)

	class Meta:
		app_label = 'core'


class Person(models.Model):
	paypal_account = models.CharField(max_length=255)
	name = models.CharField(max_length=255)

	class Meta:
		app_label = 'core'


class Offer(models.Model):
	beacon_uuid = models.CharField(max_length=255)
	beacon_minor = models.IntegerField()
	beacon_major = models.IntegerField()
	business = models.ForeignKey('Business')
	issued_date = models.DateTimeField(default=datetime.datetime.now)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=13, decimal_places=2)
	quantity = models.PositiveIntegerField()
	quantity_available = models.PositiveIntegerField()
	status = models.CharField(max_length=255, choices=(('open', 'Open'), ('closed', 'Closed')))

	class Meta:
		app_label = 'core'


class DoneDeal(models.Model):
	person = models.ForeignKey('Person')
	offer = models.ForeignKey('Offer')
	code = models.CharField(max_length=255)
	purchase_date = models.DateTimeField(default=datetime.datetime.now)

	class Meta:
		app_label = 'core'
