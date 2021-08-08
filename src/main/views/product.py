import random
import string

from django.db import models
from django.utils.text import slugify
from rest_framework import filters
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import Pagination
from ..models import Product, Subcategory, Rating
from ..serializers.product_serializer import ProductListSerializer, ProductAddSerializer


class ProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
    pagination_class = Pagination

    def get_queryset(self):
        s = get_object_or_404(Subcategory, slug=self.kwargs["subcategory"],
                              parent=self.kwargs["category"])
        return Product.objects.filter(subcategory=s, draft=False)\
            .select_related('subcategory__parent')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


class ProductGetView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        get_object_or_404(Subcategory, pk=kwargs["subcategory"],
                          parent=kwargs["category"])
        s = kwargs["subcategory"].capitalize()
        exec(f'from {kwargs["category"]}.models import {s}')
        obj = eval(f'get_object_or_404({s}.objects.select_related("product"), product=kwargs["slug"],'
                   f'product__subcategory=kwargs["subcategory"], product__draft=False)')
        exec(f'from {kwargs["category"]}.serializer import {s}Serializer')
        return eval(f'Response({s}Serializer(obj).data)')

class ProductAddView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data['author'] = request.user.id
        request.data['slug'] = slugify(request.data['title']) + \
                                          ''.join(random.choices(
                                              string.ascii_uppercase + string.ascii_lowercase + string.digits,
                                              k=6))
        s = ProductAddSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(status=201)


class ProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request.data['product']['author'] = request.user.id
        request.data['product']['slug'] = slugify(request.data['product']['title'])+ \
                     ''.join(random.choices(
                         string.ascii_uppercase + string.ascii_lowercase + string.digits,
                         k=6))
        print(request.data)
        s = request.data['product']['subcategory'].capitalize()
        exec(f"from {kwargs['category']}.serializer import {s}AddSerializer")
        serializer = eval(f"{s}AddSerializer(data=request.data)")
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201, data=request.data['product']['slug'])

    def patch(self, request, *args, **kwargs):
        kwargs['subcategory'] = kwargs['subcategory'].capitalize()
        if request.data["product"]:
            p = get_object_or_404(Product, pk=kwargs['slug'], author=request.user)
            s = ProductAddSerializer(p, data=request.data["product"],partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            request.data.pop('product')
        if request.data:
            exec(f"from {kwargs['category']}.models import {kwargs['subcategory']}")
            obj = eval(
                f"get_object_or_404({kwargs['subcategory']}.objects.select_related('product'), product=kwargs['slug'], product__author=request.user)")
            exec(f"from {kwargs['category']}.serializer import {kwargs['subcategory']}AddSerializer")
            s = eval(f"{kwargs['subcategory']}AddSerializer(obj, data=request.data, partial=True)")
            s.is_valid(raise_exception=True)
            s.save()

        return Response(status=201)

    def delete(self, request, *args, **kwargs):
        get_object_or_404(Product, pk=kwargs['slug'], author=request.user).delete()
        return Response(status=204)


class UploadImageView(APIView):
    def post(self, request, slug):
        obj = get_object_or_404(Product, slug=slug)
        print(request.data)
        obj.image = request.data['image']
        obj.save()
        return Response(status=201)


class ProductSearchView(ListAPIView):
    permission_classes = (AllowAny,)
    search_fields = ["title"]
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.filter(draft=False).select_related('subcategory')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))
