# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
import pgcrypto



@python_2_unicode_compatible
class Product(models.Model):
    PRODUCT_TYPES = (
        ('Baked Goods', 'Baked Goods'),
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Jams, Jellies, and Syrups', 'Jams, Jellies, and Syrups'),
        ('Meat', 'Meat'),
        ('Sauces', 'Sauces'),
        ('Noodles and Grains', 'Noodles and Grains'),
    )
    name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50, choices=PRODUCT_TYPES)
    winter = models.BooleanField(default=False)
    spring = models.BooleanField(default=False)
    summer = models.BooleanField(default=False)
    fall = models.BooleanField(default=False)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    owner = pgcrypto.EncryptedCharField(max_length=50, default="")
    phone_number = pgcrypto.EncryptedCharField(max_length=50, default="")
    market = models.ForeignKey('Market', on_delete=None, default=None, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Market(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Query(models.Model):
    city = models.CharField(max_length=100)
    time = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=None, default=None)

    def __str__(self):
        return self.city
