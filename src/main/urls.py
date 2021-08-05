from django.urls import path

from .views.review import ReviewAddView, ReviewListView
from .views.rating import AddStarRatingView, RatingCheckView
from .views.category import CategoryListView, CategoryChildListView
from .views.product import ProductListView, ProductView, ProductSearchView, ProductGetView


urlpatterns = [
    path('rating/', AddStarRatingView.as_view()),
    path('rating/<slug:product>/', RatingCheckView.as_view()),

    path('category/', CategoryListView.as_view()),
    path('category/<slug:slug>/', CategoryChildListView.as_view()),

    path('product/detail/<slug:category>/<slug:subcategory>/<slug:slug>/', ProductGetView.as_view()),
    path('product/list/<slug:category>/<slug:subcategory>/', ProductListView.as_view()),
    path('product/add/<slug:category>/', ProductView.as_view()),
    path('product/update/<slug:category>/<slug:subcategory>/<slug:slug>/', ProductView.as_view()),
    path('product/delete/<slug:slug>/', ProductView.as_view()),
    path('product/search/', ProductSearchView.as_view()),

    path('add/review/<slug:product>/', ReviewAddView.as_view()),
    path('list/review/<slug:product>/', ReviewListView.as_view()),
]