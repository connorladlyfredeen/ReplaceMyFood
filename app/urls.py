from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /buyer/market
    url('^buyer/market/$', views.market, name='detail'),
    url('^buyer/market$', views.market, name='detail'),
    # ex: /buyer/vendor-info
    url(r'^buyer/vendor-info/$', views.vendor_info, name='detail'),
    url(r'^buyer/vendor-info$', views.vendor_info, name='detail'),
    # ex: /buyer/
    url(r'^buyer/$', views.buyer, name='detail'),
    url(r'^buyer$', views.buyer, name='detail'),
    # ex: /vendor/
    url(r'^vendor/$', views.vendor, name='detail'),
    url(r'^vendor$', views.vendor, name='detail'),
    # ex: /polls/
    url(r'^$', views.home, name='index'),
]
