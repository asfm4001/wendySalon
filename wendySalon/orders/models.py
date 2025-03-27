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
    def to_event(self):
        match self.appointment_no:
            case '1':
                event_teitle = '第一時段已額滿'
            case '2':
                event_teitle = '第二時段已額滿'
            case '3':
                event_teitle = '第三時段已額滿'
            case _:
                event_teitle = 'Order.appointment Value Error'
        event = Event(title=event_teitle, start=self.order_date)
        return event
    
class Event(models.Model):
    title = models.CharField(max_length=20)
    start = models.DateField()
    def __str__(self):
        return self.id