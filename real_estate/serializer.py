from rest_framework import serializers

from main.serializers.product_serializer import ProductSerializer, ProductAddSerializer
from main.models import Product
from .models import Flat, Office, Sector, Vacation_home, Other_r


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


class OfficeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Office
        exclude = ('id',)

class OfficeAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Office
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Office.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class SectorSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Sector
        exclude = ('id',)

class SectorAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Sector
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Sector.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class Vacation_homeSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Vacation_home
        exclude = ('id',)

class Vacation_homeAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Vacation_home
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Vacation_home.objects.create(**validated_data, product=product)
        instance.save()
        return instance


class Other_rSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Other_r
        exclude = ('id',)

class Other_rAddSerializer(serializers.ModelSerializer):
    product = ProductAddSerializer()
    class Meta:
        model = Other_r
        fields = '__all__'

    def create(self, validated_data):
        product = Product.objects.create(**validated_data.pop('product'))
        instance = Other_r.objects.create(**validated_data, product=product)
        instance.save()
        return instance