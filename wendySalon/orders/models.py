from django.db import models
from django.contrib import admin
# Create your models here.
class Order(models.Model):
    client_name = models.CharField('客戶名稱', max_length=20)
    client_phone = models.CharField('聯絡電話', max_length=10)
    order_date = models.DateField('預約日期')
    appointment_no = models.CharField('預約時段', max_length=1)     # 預算時間(1: 09~12, 2: 13~16, 3: 17~20)
    service = models.TextField('服務項目')
    # @admin.display(
    #     boolean=True,
    #     ordering='order_date',
    # )
    def __str__(self):
        return self.client_name