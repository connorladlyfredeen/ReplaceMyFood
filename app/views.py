# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from models import *


def home(request):
    template = loader.get_template('app/home.html')
    return HttpResponse(template.render())


def vendor(request):
    return HttpResponse("This is the vendor landing page where vendors can add their products and location or a market with many vendors")


def buyer(request):
    template = loader.get_template('app/buyer.html')
    return HttpResponse(template.render())


def market(request):
    query_city = request.GET.get('city')
    print query_city
    markets = Market.objects.filter(city=query_city)[:10]
    template = loader.get_template('app/markets.html')
    context = {
        'markets': markets,
        'city': query_city,
    }
    return HttpResponse(template.render(context, request))


def product(request):
    current_month = timezone.now().month
    product_name = request.GET.get('name')
    city_name = request.GET.get('city')
    try:
        product_obj = Product.objects.get(name=product_name)
    except Product.DoesNotExist:
        product_obj = None

    product_replacements = []

    if product_obj:
        query = Query(time=timezone.now(), product=product_obj, city=city_name)
        query.save()
        if current_month <= 3:
            product_replacements = Product.objects.filter(
                product_type=product_obj.product_type, winter=True
            ).exclude(name=product_obj.name)[:10]
        elif current_month <= 6:
            product_replacements = Product.objects.filter(
                product_type=product_obj.product_type, spring=True
            ).exclude(name=product_obj.name)[:10]
        elif current_month <= 9:
            product_replacements = Product.objects.filter(
                product_type=product_obj.product_type, summer=True
            ).exclude(name=product_obj.name)[:10]
        else:
            product_replacements = Product.objects.filter(
                product_type=product_obj.product_type, fall=True
            ).exclude(name=product_obj.name)[:10]

    context = {
        'product': product_obj,
        'product_name': product_name,
        'product_replacements': product_replacements,
    }
    template = loader.get_template('app/product.html')
    return HttpResponse(template.render(context, request))
