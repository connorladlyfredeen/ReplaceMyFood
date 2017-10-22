# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    winter = models.BooleanField(default=False)
    spring = models.BooleanField(default=False)
    summer = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Market(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Query(models.Model):
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.address
