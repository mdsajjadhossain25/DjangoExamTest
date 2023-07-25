from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CatShop

class CatAPITests(APITestCase):
    def setUp(self):
        self.cat = CatShop.objects.create(name='Test Cat', price=2)
    
    def test_cat_list(self):
        url = reverse('cat-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_cat_detail(self):
        url = reverse('cat-detail', kwargs={'pk': self.cat.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Cat')
        
    def test_create_cat(self):
        url = reverse('cat-list')
        data = {'name': 'Husky Name', 'price': 3, 'breed' : 'Husky', 'description':'Hello'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CatShop.objects.count(), 2)
        self.assertEqual(CatShop.objects.last().name, 'Husky Name')