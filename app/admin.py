# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Market)
admin.site.register(Query)
