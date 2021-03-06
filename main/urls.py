from django.urls import path, include

from .views.review import ReviewAddView, ReviewListView
from .views.rating import AddStarRatingView, RatingCheckView
from .views.category import CategoryListView, CategoryChildListView, CityListView
from .views.product import (ProductListView, ProductView, ProductSearchView,
                            UploadImageView, MyProductsView, MainPageProductListView,
                            FavouriteView, SimilarProductListView, SearchAllView, MapView)


urlpatterns = [
    #path('add/', ProductAddView.as_view()),
    path('rating/', AddStarRatingView.as_view()),
    path('rating/<slug:product>/', RatingCheckView.as_view()),

    path('category/', CategoryListView.as_view()),
    path('category/<slug:slug>/', CategoryChildListView.as_view()),
    path('city/', CityListView.as_view()),

    path('main/', MainPageProductListView.as_view()),
    path('my/', MyProductsView.as_view()),
    path('real_estate/', include('real_estate.urls')),
    path('transport/', include('transport.urls')),

    #path('product/detail/<slug:category>/<slug:subcategory>/<slug:slug>/', ProductGetView.as_view()),
    path('product/list/<slug:category>/<slug:subcategory>/', ProductListView.as_view()),
    #path('product/add/<slug:category>/', ProductView.as_view()),
    #path('product/update/<slug:category>/<slug:subcategory>/<slug:slug>/', ProductView.as_view()),
    path('product/delete/<slug:slug>/', ProductView.as_view()),
    path('search/all/', SearchAllView.as_view()),
    path('search/<slug:subcategory>/', ProductSearchView.as_view()),
    path('upload_image/<slug:slug>/', UploadImageView.as_view()),
    path('favorite/', FavouriteView.as_view()),
    path('similar/<slug:subcategory>/<slug:slug>/', SimilarProductListView.as_view()),

    path('review/add/<slug:product>/', ReviewAddView.as_view()),
    path('review/list/<slug:product>/', ReviewListView.as_view()),

    path('map/<slug:city>/', MapView.as_view()),
]
