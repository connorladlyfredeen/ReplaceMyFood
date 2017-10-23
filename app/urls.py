from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /buyer/market
    url('^buyer/market/$', views.market, name='markets'),
    url('^buyer/market$', views.market, name='markets'),
    # ex: /buyer/vendor-info
    url(r'^buyer/product/$', views.product, name='product'),
    url(r'^buyer/product$', views.product, name='product'),
    # ex: /buyer/
    url(r'^buyer/$', views.buyer, name='buyer-home'),
    url(r'^buyer$', views.buyer, name='buyer-home'),
    # ex: /vendor/
    url(r'^vendor/$', views.vendor, name='vendor-home'),
    url(r'^vendor$', views.vendor, name='vendor-home'),
    # ex: /polls/
    url(r'^$', views.home, name='index'),
]
