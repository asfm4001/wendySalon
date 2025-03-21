from django.test import TestCase
# Create your tests here.

from django.urls import reverse
class IndexVeiwTests(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)