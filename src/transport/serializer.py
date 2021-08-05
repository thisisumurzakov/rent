from rest_framework import serializers

from main.serializers.product_serializer import ProductSerializer, ProductAddSerializer
from .models import Car


class CarSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Car
        exclude = ('id',)


class CarAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Car
        exclude = ('id',)