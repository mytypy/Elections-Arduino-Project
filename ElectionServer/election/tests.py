from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from mixins.test_mixin import TestMixin


class ElectionTests(APITestCase, TestMixin):
    def setUp(self):
        self.client = APIClient()
        self.init()
        
    def test_elections(self):
        url = reverse('election-elections')
        response = self.client.get(url, headers={'Hash': self.hash})
        
        self.assertEqual(response.status_code, 200)
        pars = response.json()['response']
        sps = pars[0]

        idd = sps['id']
        election = sps['election']
        
        self.assertEqual((idd, election), (1, 'Тут наверное что-то есть'))
    
    def test_delete(self):
        url = reverse('election-delete-election')
        data = {'id': 1}
        
        response = self.client.delete(url, data=data, headers={'Hash': self.hash})
        self.assertEqual(response.status_code, 200)