from django.urls import path

from .views.flat import FlatGetView, FlatView
from .views.office import OfficeGetView, OfficeView
from .views.other_r import Other_rGetView, Other_rView
from .views.sector import SectorGetView, SectorView
from .views.vacation_home import Vacation_homeGetView, Vacation_homeView

urlpatterns = [
    path('flat/add/', FlatView.as_view()),
    path('flat/update/<slug:slug>/', FlatView.as_view()),
    path('flat/detail/<slug:slug>/', FlatGetView.as_view()),

    path('office/add/', OfficeView.as_view()),
    path('office/update/<slug:slug>/', OfficeView.as_view()),
    path('office/detail/<slug:slug>/', OfficeGetView.as_view()),

    path('other_r/add/', Other_rView.as_view()),
    path('other_r/update/<slug:slug>/', Other_rView.as_view()),
    path('other_r/detail/<slug:slug>/', Other_rGetView.as_view()),

    path('sector/add/', SectorView.as_view()),
    path('sector/update/<slug:slug>/', SectorView.as_view()),
    path('sector/detail/<slug:slug>/', SectorGetView.as_view()),

    path('vacation_home/add/', Vacation_homeView.as_view()),
    path('vacation_home/update/<slug:slug>', Vacation_homeView.as_view()),
    path('vacation_home/detail/<slug:slug>', Vacation_homeGetView.as_view()),
]
