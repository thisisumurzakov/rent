from django_filters import rest_framework as filters

from main.models import Product


class flatFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class officeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class other_rFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class sectorFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class vacation_homeFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='gte')
    max_area = filters.NumberFilter(field_name="flats__total_area", lookup_expr='lte')
    search = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['search', 'min_price', 'max_price', 'min_area', 'max_area', 'city', 'flats__rooms', 'flats__floor']


class carFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']


class truckFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']


class agriculturalFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']


class specialFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']


class other_tFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'min_price', 'max_price', 'city', 'cars__color', 'cars__fuel_type', 'cars__mileage', 'cars__transmission']
