from rest_framework import serializers
from orders.models import Order
from django.utils import timezone

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'    # 選取所有column
        # fields = ('id', 'client_name', 'order_date', 'appointment_no')