from django.urls import path

from .views.views import BrandListView, ModelListView, ColorListView, BodyTypeListView
from .views.car import CarView, CarGetView
from .views.agricultural import AgriculturalView, AgriculturalGetView
from .views.other_t import Other_tView, Other_tGetView
from .views.special import SpecialView, SpecialGetView
from .views.truck import TruckView, TruckGetView

urlpatterns = [
    path('brand/', BrandListView.as_view()),
    path('model/<slug:brand>/', ModelListView.as_view()),
    path('color/', ColorListView.as_view()),
    path('body_type/', BodyTypeListView.as_view()),

    path('agricultural/add/', AgriculturalView.as_view()),
    path('agricultural/update/<slug:slug>/', AgriculturalView.as_view()),
    path('agricultural/detail/<slug:slug>/', AgriculturalGetView.as_view()),

    path('car/add/', CarView.as_view()),
    path('car/update/<slug:slug>/', CarView.as_view()),
    path('car/detail/<slug:slug>/', CarGetView.as_view()),

    path('other_t/add/', Other_tView.as_view()),
    path('other_t/update/<slug:slug>/', Other_tView.as_view()),
    path('other_t/detail/<slug:slug>/', Other_tGetView.as_view()),

    path('special/add/', SpecialView.as_view()),
    path('special/update/<slug:slug>/', SpecialView.as_view()),
    path('special/detail/<slug:slug>/', SpecialGetView.as_view()),

    path('truck/add/', TruckView.as_view()),
    path('truck/update/<slug:slug>/', TruckView.as_view()),
    path('truck/detail/<slug:slug>/', TruckGetView.as_view()),
]
