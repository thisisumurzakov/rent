from rest_framework import serializers

from main.serializers.product_serializer import ProductSerializer, ProductAddSerializer
from main.models import Product
from .models import Flat


class FlatSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Flat
        exclude = ('id',)

class FlatAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Flat
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Flat.objects.create(**validated_data, product=product)
        instance.save()
        return instance