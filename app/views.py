# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('app/home.html')
    return HttpResponse(template.render())


def vendor(request):
    return HttpResponse("This is the vendor landing page where vendors can add their products and location or a market with many vendors")


def buyer(request):
    return HttpResponse("this is the buyer page. ")


def market(request):
    return HttpResponse("this is the page for a market where you can see all of the produce available at that market")


def vendor_info(request):
    return HttpResponse("This page will show all vendors that match your preferences")
