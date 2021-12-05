from django.urls import path

from .views import BrandListView, ModelListView, ColorListView, BodyTypeListView

urlpatterns = [
    path('brand/', BrandListView.as_view()),
    path('model/<slug:brand>/', ModelListView.as_view()),
    path('color/', ColorListView.as_view()),
    path('body_type/', BodyTypeListView.as_view()),
]
