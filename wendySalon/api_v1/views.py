from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from orders.models import Order
from .serializers import OrderSerializer, EventSerializer
# class OrderViewSets(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     def get_queryset(self):
#         queryset = Order.objects.all()
#         return queryset
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from django.utils import timezone
class OrderToEventViewSets(GenericAPIView):
    events = []
    for order in Order.objects.all():
        if order.order_date >= timezone.now().date():
            events.append(order.to_event())
        
    queryset = events
    serializer_class = EventSerializer
    def get(self, request, *args, **krgs):
        events = self.get_queryset()
        serializer = self.serializer_class(events, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)
