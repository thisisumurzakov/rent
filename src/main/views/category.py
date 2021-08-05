from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

from ..models import Category, Subcategory
from ..serializers.category_serializer import CategoryListSerializer, CategoryChildListSerializer


class CategoryListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryChildListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CategoryChildListSerializer

    def get_queryset(self):
        get_object_or_404(Category, slug=self.kwargs["slug"])
        return Subcategory.objects.filter(parent__slug=self.kwargs["slug"])
