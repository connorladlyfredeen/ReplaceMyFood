from controlcenter import Dashboard, widgets
from app.models import Query, Product, Vendor
from django.db.models import Count


class MostCommonQueriedCities(widgets.ItemList):
    model = Query
    queryset = Query.objects.all().values('city').annotate(total=Count('city')).order_by('-total')[:10]
    list_display = ('city', 'total')


class MostCommonQueriedProducts(widgets.ItemList):
    model = Query
    queryset = Query.objects.all().values('product').annotate(total=Count('product')).order_by('-total')[:10]
    list_display = ('get_name', 'total')

    def get_name(self, obj):
        product = Product.objects.get(pk=obj['product'])
        return product


class LastTenQueries(widgets.ItemList):
    model = Query
    queryset = Query.objects.order_by('-time')[:10]
    list_display = ('product', 'total')


class MyDashboard(Dashboard):
    widgets = (
        MostCommonQueriedCities,
        MostCommonQueriedProducts,
        LastTenQueries,
    )
