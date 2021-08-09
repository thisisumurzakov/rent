from rest_framework import serializers

from ..models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugField(source="subcategory.parent.slug")
    avarege_star = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ('image', 'title', 'slug', 'price', 'city', 'publish',
                  'updated', 'subcategory', 'category', 'avarege_star')


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    id = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Product
        exclude = ('subcategory', 'draft')

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('publish', 'created', 'updated', 'image')