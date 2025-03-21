from django.test import TestCase

# Create your tests here.
from django.utils import timezone
from .models import Order
# class OrderModelTest(TestCase):
#     def test_order(self):
#         order = Order(
#             client_name = '測試用戶',
#             client_phone = '0912345678',
#             order_date = timezone,
#             appointment_no = '1',
#             service = '測試服務項目'
#         )