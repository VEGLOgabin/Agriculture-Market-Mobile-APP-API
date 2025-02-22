from django.contrib import admin
from django.urls import path, include
from .swagger import schema_view
import api.urls 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('auth/', include('djoser.urls')),  
    path('auth/', include('djoser.urls.jwt')),  
    path("api/", include(api.urls)),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


