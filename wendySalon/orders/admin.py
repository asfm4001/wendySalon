from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('聯絡資訊', {'fields': ['client_name', 'client_phone']}),
        ("Detail", {
            'fields': ['order_date', 'appointment_no', 'service'], 
            'classes': ['collape']
            })
    ]
    list_display = ['client_name', 'client_phone', 'order_date', 'appointment_no']
    list_filter = ["order_date"]

admin.site.register(Order, OrderAdmin)