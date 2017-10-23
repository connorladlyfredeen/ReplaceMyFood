from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /buyer/market
    url('^buyer/market/$', views.market, name='markets'),
    url('^buyer/market$', views.market, name='markets-1'),
    # ex: /buyer/vendor-info
    url(r'^buyer/product/$', views.product, name='product'),
    url(r'^buyer/product$', views.product, name='product-1'),
    # ex: /buyer/
    url(r'^buyer/$', views.buyer, name='buyer'),
    url(r'^buyer$', views.buyer, name='buyer-1'),
    # ex: /vendor/
    url(r'^vendor/product/$', views.add_product, name='vendor-product'),
    url(r'^vendor/product$', views.add_product, name='vendor-product-1'),
    # ex: /vendor/
    url(r'^vendor/add/$', views.add_or_update_vendor, name='vendor-add'),
    url(r'^vendor/add$', views.add_or_update_vendor, name='vendor-add-1'),
    # ex: /vendor/
    url(r'^vendor/delete/$', views.delete_vendor, name='vendor-delete'),
    url(r'^vendor/delete$', views.delete_vendor, name='vendor-delete-1'),
    # ex: /vendor/
    url(r'^vendor/$', views.vendor, name='vendor'),
    url(r'^vendor$', views.vendor, name='vendor-1'),
    # ex: /polls/
    url(r'^$', views.home, name='index'),
]
