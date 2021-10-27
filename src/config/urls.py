import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('main.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)