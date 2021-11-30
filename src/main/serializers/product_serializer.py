from rest_framework import serializers

from ..models import Product, Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('media',)


class MediaAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugField(source="subcategory.parent.slug")
    avarege_star = serializers.IntegerField()
    media = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ('media', 'title', 'slug', 'price', 'city', 'publish',
                  'updated', 'subcategory', 'category', 'avarege_star')

    def get_media(self, instance):
        image = instance.media.first()
        return MediaSerializer(image).data


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    id = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True, read_only=True)
    author = AuthorSerializer()
    class Meta:
        model = Product
        exclude = ('subcategory', 'draft')

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('publish', 'created', 'updated')