from django.urls import path
from . import views

urlpatterns = [
    path('', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger<format>/', views.schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('redoc/', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]