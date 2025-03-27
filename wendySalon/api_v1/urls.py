from django.urls import path
from . import views

app_name = 'api_v1'
urlpatterns = [
    path('orders_to_events/', views.OrderToEventViewSets.as_view(), name='orders_to_events'),
]
