from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.review_serializer import ReviewAddSerializer, ReviewSerializer
from ..models import Product, Review

class ReviewAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        get_object_or_404(Product, slug=kwargs["product"])
        request.data["product"] = kwargs["product"]
        request.data["user"] = request.user.id
        s = ReviewAddSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(status=201)


class ReviewListView(APIView):
    def get(self, request, *args, **kwargs):
        r = Review.objects.filter(product=kwargs["product"])
        return Response(ReviewSerializer(r, many=True).data)