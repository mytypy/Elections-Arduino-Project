import os
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from main.models import UserModel
from mixins.test_mixin import TestMixin


class MainTests(APITestCase, TestMixin):
    def setUp(self):
        self.client = APIClient()
        self.init()
    
    def test_response(self):
        url = 'http://127.0.0.1:8000/'
        
        response_before = self.client.get(url)
        self.assertEqual(response_before.status_code, 403)

        response_after = self.client.get(url, headers=self.headers)
        self.assertEqual(response_after.status_code, 404)
        
    def test_create_election(self):
        url = reverse('user-post-user-election') # Т.к я использую ModelViewSet, то я должен писать в таком формате "basename-action-my-method"(Все через тире, даже нижнее подчеркивание)
        response_null = self.client.post(url, self.data_null_1, format='json', headers=self.headers)
        self.assertEqual(response_null.json()['response'], 'Запись добавлена')
        
        user = UserModel.objects.get(id_card=self.id_card).__dict__.values()
        self.assertEqual(list(user)[2:], list(self.data_null_1.values()))