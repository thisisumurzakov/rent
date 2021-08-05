import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += doc_url