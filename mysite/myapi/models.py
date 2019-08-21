# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hero(models.Model):
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)
	
	def __str__(self):
		return self.name
	
class Address(models.Model):
	address = models.CharField(max_length=60)
	zip = models.CharField(max_length=10)
	
	def __str__(self):
		return self.address
	

