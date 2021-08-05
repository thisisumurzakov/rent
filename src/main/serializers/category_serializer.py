from rest_framework import serializers
from ..models import Category, Subcategory


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryChildListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        exclude = ('parent', )
