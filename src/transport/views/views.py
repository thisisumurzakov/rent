from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import AllowAny

from ..models import Brand, Model, Color, BodyType
from ..serializer import BrandListSerializer, ModelListSerializer, ColorListSerializer, BodyTypeListSerializer


class BrandListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


class ModelListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ModelListSerializer

    def get_queryset(self):
        return Model.objects.filter(brand__slug=self.kwargs["brand"])


class ColorListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ColorListSerializer
    queryset = Color.objects.all()


class BodyTypeListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = BodyTypeListSerializer
    queryset = BodyType.objects.all()