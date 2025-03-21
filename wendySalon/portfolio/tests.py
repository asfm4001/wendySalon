from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Portfolio
import os

class ProtfolioVeiwTest(TestCase):
    def test_no_portfolio(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)

    def test_has_portfolio(self):
            # upload
            image_data = SimpleUploadedFile(
                'test_image.jpg',
                b'file_content',   # 檔案內容（二進制）
                content_type='image/jpeg'  # 圖片格式
            )

            # 創建 Portfolio
            portfolio = Portfolio.objects.create(
                title='測試作品1', 
                context='測試作品1內容', 
                img=image_data
            )

            response = self.client.get(reverse('portfolio:index'))
            self.assertEqual(response.status_code, 200)
            # Portfolio.img路徑
            self.assertEqual(portfolio.img.url, '/mdeia/portfolio/test_image.jpg')
    
    def tearDown(self):
        """ 測試完成後，刪除測試用的文件（如果存在）"""
        test_image_path = os.path.join(settings.MEDIA_ROOT, 'portfolio/test_image.jpg')
        if os.path.exists(test_image_path):
            os.remove(test_image_path)
            