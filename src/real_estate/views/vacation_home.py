import random
import string

from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Subcategory, Product
from ..models import Vacation_home
from ..serializer import Vacation_homeSerializer, Vacation_homeAddSerializer
from main.serializers.product_serializer import ProductAddSerializer


class Vacation_homeGetView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Vacation_home.objects.select_related("product"),
                                product__slug=kwargs["slug"], product__draft=False)
        data = Vacation_homeSerializer(obj).data
        if request.user in obj.product.favourite.all():
            data["is_favourite"] = True
        else:
            data["is_favourite"] = False
        return Response(data)


class Vacation_homeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = Vacation_homeAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['product']['author'] = request.user
        serializer.validated_data['product']['slug'] = slugify(request.data['product']['title']) + \
                                                       ''.join(random.choices(
                                                           string.ascii_uppercase + string.ascii_lowercase + string.digits,
                                                           k=6))
        serializer.save()
        return Response(status=201, data=serializer.validated_data['product']['slug'])

    def patch(self, request, *args, **kwargs):
        kwargs['subcategory'] = kwargs['subcategory'].capitalize()
        if "product" in request.data:
            p = get_object_or_404(Product, slug=kwargs['slug'], author=request.user)
            s = ProductAddSerializer(p, data=request.data["product"],partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            request.data.pop('product')
        if request.data:
            obj = get_object_or_404(Vacation_home.objects.select_related('product'), product__slug=kwargs['slug'], product__author=request.user)
            s = Vacation_homeAddSerializer(obj, data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()

        return Response(status=201)