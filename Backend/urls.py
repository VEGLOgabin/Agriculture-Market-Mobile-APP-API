from django.contrib import admin
from django.urls import path, include
from .swagger import schema_view
import api.urls 

urlpatterns = [
    path('auth/', include('djoser.urls')),  
    path('auth/', include('djoser.urls.jwt')),  
    path("api/", include(api.urls)),
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
]


