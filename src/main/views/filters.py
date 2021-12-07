from django_filters import rest_framework as filters

from main.models import Product


class FlatFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class OfficeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="offices__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="offices__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'offices__rooms', 'offices__floor']


class Other_rFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="other_rs__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="other_rs__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'other_rs__rooms', 'other_rs__floor']


class SectorFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="sectors__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="sectors__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'sectors__rooms', 'sectors__floor']


class Vacation_homeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="vacation_homes__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="vacation_homes__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'vacation_homes__rooms', 'vacation_homes__floor']


class CarFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']


class TruckFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'trucks__color', 'trucks__fuel_type', 'trucks__mileage', 'trucks__transmission']


class AgriculturalFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'agriculturals__color', 'agriculturals__fuel_type', 'agriculturals__mileage', 'agriculturals__transmission']


class SpecialFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'specials__color', 'specials__fuel_type', 'specials__mileage', 'specials__transmission']


class Other_tFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'other_ts__color', 'other_ts__fuel_type', 'other_ts__mileage', 'other_ts__transmission']
