from rest_framework import serializers

from ..models import Review


class ReviewAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecrusiveSerializer(serializers.Serializer):
    def to_representation(self, instance):
        s = self.parent.parent.__class__(instance, context=self.context)
        return s.data


class ReviewSerializer(serializers.ModelSerializer):
    children = RecrusiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewSerializer
        model = Review
        fields = ("user", "text", "children")