from rest_framework import serializers

from main.serializers.product_serializer import ProductSerializer, ProductAddSerializer
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
        exclude = ('id',)