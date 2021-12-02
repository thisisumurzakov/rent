from rest_framework import serializers

from main.serializers.product_serializer import ProductSerializer, ProductAddSerializer
from .models import Car, Truck, Agricultural, Special, Other_t
from ..main.models import Product


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

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Car.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class TruckSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Truck
        exclude = ('id',)


class TruckAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Truck
        exclude = ('id',)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Truck.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class AgriculturalSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Agricultural
        exclude = ('id',)


class AgriculturalAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Agricultural
        exclude = ('id',)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Agricultural.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class SpecialSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Special
        exclude = ('id',)


class SpecialAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Special
        exclude = ('id',)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Special.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class Other_tSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Other_t
        exclude = ('id',)


class Other_tAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Other_t
        exclude = ('id',)

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Other_t.objects.create(**validated_data, product=product)
        instance.save()
        return instance