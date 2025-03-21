from django.test import TestCase

# Create your tests here.
import datetime
from django.urls import reverse
from django.utils import timezone
from .models import Post

def create_post(post_title, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(title=post_title, published_date=time)

class IndexVeiwTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
    
    def test_no_posts(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_post_list'], [])

    def test_has_posts(self):
        post_1 = create_post('測試公告1', -20)
        post_2 = create_post('測試公告2', 0)
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context['latest_post_list'], [post_2, post_1],)

class DetailVeiwTest(TestCase):
    def test_no_detail_page(self):
        response = self.client.get(reverse('news:detail', args=(1,)))
        self.assertEqual(response.status_code, 404)
        
    def test_has_detail_page(self):
        post_1 = create_post('測試公告1', -20)
        post_2 = create_post('測試公告2', 0)
        response = self.client.get(reverse('news:detail', args=(post_1.id,)))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('news:detail', args=(post_2.id,)))
        self.assertEqual(response.status_code, 200)