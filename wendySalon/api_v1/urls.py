from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.OrderViewSets.as_view())
]
