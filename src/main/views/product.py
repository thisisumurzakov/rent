import random
import string

from django.db import models, transaction
from django.db.models import Q
from django.utils.text import slugify
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters as rest_filter

from .filters import *
from django_filters import rest_framework as filters
from .pagination import Pagination
from ..models import Product, Subcategory, Rating
from ..serializers.product_serializer import ProductListSerializer, ProductAddSerializer, MediaAddSerializer


class MainPageProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
    pagination_class = Pagination
    def get_queryset(self):
        return Product.objects.filter(draft=False).order_by('-publish')\
            .select_related('subcategory__parent').select_related('city').prefetch_related('media')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


class ProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return Product.objects.filter(subcategory=self.kwargs["subcategory"], draft=False).order_by('-publish')\
            .select_related('subcategory__parent').select_related('city').prefetch_related('media')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


class MyProductsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductListSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user).order_by('-publish')\
            .select_related('subcategory__parent').select_related('city').prefetch_related('media')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


# class ProductGetView(APIView):
#     permission_classes = (AllowAny,)

#     def get(self, request, *args, **kwargs):
#         get_object_or_404(Subcategory, pk=kwargs["subcategory"],
#                           parent=kwargs["category"])
#         s = kwargs["subcategory"].capitalize()
#         exec(f'from {kwargs["category"]}.models import {s}')
#         obj = eval(f'get_object_or_404({s}.objects.select_related("product"), product__slug=kwargs["slug"],'
#                    f'product__subcategory=kwargs["subcategory"], product__draft=False)')
#         exec(f'from {kwargs["category"]}.serializer import {s}Serializer')
#         data = eval(f'{s}Serializer(obj).data')
#         if request.user in obj.product.favourite.all():
#             data["is_favourite"] = True
#         else:
#             data["is_favourite"] = False
#         return Response(data)

# class ProductAddView(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def post(self, request, *args, **kwargs):
#         request.data['author'] = request.user.id
#         request.data['slug'] = slugify(request.data['title']) + \
#                                           ''.join(random.choices(
#                                               string.ascii_uppercase + string.ascii_lowercase + string.digits,
#                                               k=6))
#         s = ProductAddSerializer(data=request.data)
#         s.is_valid(raise_exception=True)
#         s.save()
#         return Response(status=201)


class ProductView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        get_object_or_404(Product, slug=kwargs['slug'], author=request.user).delete()
        return Response(status=204)

    # def post(self, request, *args, **kwargs):
    #     with transaction.atomic():
    #         try:
    #             request.data['product']['author'] = request.user.id
    #             request.data['product']['slug'] = slugify(request.data['product']['title'])+ \
    #                          ''.join(random.choices(
    #                              string.ascii_uppercase + string.ascii_lowercase + string.digits,
    #                              k=6))
    #             s = request.data['product']['subcategory'].capitalize()
    #             exec(f"from {kwargs['category']}.serializer import {s}AddSerializer")
    #             serializer = eval(f"{s}AddSerializer(data=request.data)")
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()
    #             return Response(status=201, data=request.data['product']['slug'])
    #         except KeyError:
    #             return Response(status=400, data="Key error")
    #
    # def patch(self, request, *args, **kwargs):
    #     kwargs['subcategory'] = kwargs['subcategory'].capitalize()
    #     if "product" in request.data:
    #         p = get_object_or_404(Product, slug=kwargs['slug'], author=request.user)
    #         s = ProductAddSerializer(p, data=request.data["product"],partial=True)
    #         s.is_valid(raise_exception=True)
    #         s.save()
    #         request.data.pop('product')
    #     if request.data:
    #         exec(f"from {kwargs['category']}.models import {kwargs['subcategory']}")
    #         obj = eval(
    #             f"get_object_or_404({kwargs['subcategory']}.objects.select_related('product'), product__slug=kwargs['slug'], product__author=request.user)")
    #         exec(f"from {kwargs['category']}.serializer import {kwargs['subcategory']}AddSerializer")
    #         s = eval(f"{kwargs['subcategory']}AddSerializer(obj, data=request.data, partial=True)")
    #         s.is_valid(raise_exception=True)
    #         s.save()
    #
    #     return Response(status=201)


class UploadImageView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request, slug):
        print(request.data)
        if 'media[]' in request.data:
            media = request.data.pop('media[]')
            if len(media) > 5:
                return Response(status=400)
            product = get_object_or_404(Product, slug=slug)
            for m in media:
                ms = MediaAddSerializer(data={"media": m, "product": product.id})
                ms.is_valid(raise_exception=True)
                ms.save()
            return Response(status=201)
        return Response(status=400)


class SearchAllView(ListAPIView):
    search_fields = ["title"]
    filter_backends = (rest_filter.SearchFilter,)
    pagination_class = Pagination
    serializer_class = ProductListSerializer

    def get_queryset(self):
        return Product.objects.filter(draft=False).order_by('-publish').select_related('subcategory')\
            .select_related('city').prefetch_related('media') \
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


class ProductSearchView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        filterset_class = eval(f'{self.kwargs["subcategory"]}Filter')
        return Product.objects.filter(draft=False, subcategory=self.kwargs["subcategory"]).order_by('-publish').select_related('subcategory').select_related('city').prefetch_related('media')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))


class FavouriteView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = Pagination

    def get(self, request):
        return Response(status=200, data=
        ProductListSerializer(request.user.fav_posts.all()\
            .select_related('subcategory__parent')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))), many=True).data)

    def post(self, request):
        Product.objects.get(slug=request.data['slug']).favourite.add(request.user)
        return Response(status=200)

    def delete(self, request):
        Product.objects.get(slug=request.data['slug']).favourite.remove(request.user)
        return Response(status=200)


class SimilarProductListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer
    pagination_class = Pagination
    def get_queryset(self):
        return Product.objects.filter(~Q(slug=self.kwargs['slug']),draft=False, tags__name__in=self.request.data['tags'], subcategory=self.kwargs['subcategory']).distinct().order_by('-publish')\
            .select_related('subcategory__parent').select_related('city').prefetch_related('media')\
            .annotate(avarege_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings')))
