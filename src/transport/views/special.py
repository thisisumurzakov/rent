import random
import string

from django.db import transaction
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Subcategory, Product
from ..models import Special
from ..serializer import SpecialSerializer, SpecialAddSerializer
from main.serializers.product_serializer import ProductAddSerializer


class SpecialGetView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Special.objects.select_related("product"),
                                product__slug=kwargs["slug"], product__draft=False)
        data = SpecialSerializer(obj).data
        if request.user in obj.product.favourite.all():
            data["is_favourite"] = True
        else:
            data["is_favourite"] = False
        return Response(data)


class SpecialView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = SpecialAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['product']['author'] = request.user.id
        serializer.validated_data['product']['slug'] = slugify(request.data['product']['title']) + \
                                                       ''.join(random.choices(
                                                           string.ascii_uppercase + string.ascii_lowercase + string.digits,
                                                           k=6))
        serializer.save()
        return Response(status=201, data=request.data['product']['slug'])

    def patch(self, request, *args, **kwargs):
        kwargs['subcategory'] = kwargs['subcategory'].capitalize()
        if "product" in request.data:
            p = get_object_or_404(Product, slug=kwargs['slug'], author=request.user)
            s = ProductAddSerializer(p, data=request.data["product"],partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            request.data.pop('product')
        if request.data:
            obj = get_object_or_404(Special.objects.select_related('product'), product__slug=kwargs['slug'], product__author=request.user)
            s = SpecialAddSerializer(obj, data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

        return Response(status=201)