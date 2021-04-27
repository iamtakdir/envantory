import django_filters
from django_filters import CharFilter

from .models import Stock

class Filter(django_filters.FilterSet):

    name=CharFilter(field_name='item_name' , lookup_expr='icontains')
    
    class Meta:
        model = Stock
        fields = ['name', 'category','supplier']
