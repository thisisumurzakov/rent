from rest_framework import serializers
from ..models import Category, Subcategory, City


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryChildListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ('parent', )


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
