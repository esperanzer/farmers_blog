# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class product(models.Model):
	product_name = models.CharField(max_length= 55)
	farm_name = models.CharField(max_length=55)
	product_logo = models.CharField(max_length=400)
	Country = models.CharField(max_length= 20)

	#def__str__ (self)

