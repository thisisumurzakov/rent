from rest_framework import serializers

from ..models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugField(source="subcategory.parent.slug")
    middle_star = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('image', 'title', 'slug', 'price', 'city', 'publish',
                  'updated', 'subcategory', 'category', "middle_star")


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.__str__')
    class Meta:
        model = Product
        exclude = ('subcategory', 'draft')

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('publish', 'created', 'updated')