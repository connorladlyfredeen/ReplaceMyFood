# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.shortcuts import render

# Create your views here.
from models import *


def home(request):
    return render(request, 'app/home.html')


def vendor(request):
    return render(request, 'app/vendor.html')


def add_or_update_vendor(request):
    if not Market.objects.filter(name=request.POST.get('market')).exists():
        new_market = Market(
            name=request.POST.get('market'),
            city=request.POST.get('city'),
            address=request.POST.get('address')
        )
        new_market.save()
        vendor_market = new_market
    else:
        vendor_market = Market.pbjects.get(name=request.POST.get('market'))
    if Vendor.objects.filter(name=request.POST.get('name')).exists():
        vendor_obj = Vendor.objects.get(name=request.POST.get('name'))
        if vendor_obj.phone_number != request.POST.get('phone'):
            return render(request, 'app/vendor.html', {'message': 'You are not authorized', 'colour': 'red'})
        vendor_obj.market = vendor_market
        if len(request.POST.get('owner')) != 0:
            vendor_obj.owner = request.POST.get('owner')
        vendor_obj.save()
        return render(request, 'app/vendor.html', {'message': 'Successfully updated vendor', 'colour': 'green'})

    # Not an update, so create new
    vendor_obj = Vendor(
        phone_number=request.POST.get('phone'),
        owner=request.POST.get('owner'),
        market=vendor_market,
        name=request.POST.get('name')
    )
    vendor_obj.save()
    return render(request, 'app/vendor.html', {'message': 'Successfully added new vendor', 'colour': 'green'})


def delete_vendor(request):
    if not Vendor.objects.filter(name=request.POST.get('name')).exists():
        return render(request, 'app/vendor.html', {'message': 'Vendor does not exist', 'colour': 'red'})
    vendor_obj = Vendor.objects.get(name=request.POST.get('name'))
    if vendor_obj.phone_number != request.POST.get('phone'):
        return render(request, 'app/vendor.html', {'message': 'You are not authorized', 'colour': 'red'})
    vendor_obj.delete()
    return render(request, 'app/vendor.html', {'message': 'Success', 'colour': 'green'})


def buyer(request):
    return render(request, 'app/buyer.html')


def market(request):
    query_city = request.GET.get('city')
    markets = Market.objects.filter(city=query_city)[:10]
    return render(request, 'app/markets.html', {
        'markets': markets,
        'city': query_city,
    })


def add_product(request):
    if Product.objects.filter(name=request.POST.get('name')).exists():
        return render(request, 'app/vendor.html', {'message': 'Product already exists', 'colour': 'red'})
    winter_bool = 'Winter' in request.POST.get('season', [])
    spring_bool = 'Spring' in request.POST.get('season', [])
    summer_bool = 'Summer' in request.POST.get('season', [])
    fall_bool = 'Fall' in request.POST.get('season', [])
    new_product = Product(
        name=request.POST['name'],
        product_type=request.POST.get('product_type'),
        winter=winter_bool,
        spring=spring_bool,
        summer=summer_bool,
        fall=fall_bool
    )
    new_product.save()
    return render(request, 'app/vendor.html', {'message': 'Successfully added the product', 'colour': 'green'})


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
            product_replacements = Product.objects.filter(product_type=product_obj.product_type, winter=True)[:10]
        elif current_month <= 6:
            product_replacements = Product.objects.filter(product_type=product_obj.product_type, spring=True)[:10]
        elif current_month <= 9:
            product_replacements = Product.objects.filter(product_type=product_obj.product_type, summer=True)[:10]
        else:
            product_replacements = Product.objects.filter(product_type=product_obj.product_type, fall=True)[:10]

    return render(request, 'app/product.html', {
        'product': product_obj,
        'product_name': product_name,
        'product_replacements': product_replacements,
    })
