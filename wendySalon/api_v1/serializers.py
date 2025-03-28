from rest_framework import serializers
from orders.models import Order, Event

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'    # 選取所有column
        # fields = ('id', 'client_name', 'order_date', 'appointment_no')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        # fields = '__all__'
        fields = ('title', 'start')