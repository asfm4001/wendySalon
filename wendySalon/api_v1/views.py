from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from orders.models import Order
from .serializers import OrderSerializer
# class OrderViewSets(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     def get_queryset(self):
#         queryset = Order.objects.all()
#         return queryset
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
class OrderViewSets(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def get(self, request, *args, **krgs):
        orders = self.get_queryset()
        serializer = self.serializer_class(orders, many=True)
        data = serializer.data
        return JsonResponse(data, safe=False)