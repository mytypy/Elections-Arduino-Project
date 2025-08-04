from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from mixins.test_mixin import TestMixin
from election.models import ElectionModel
from choice.models import ChoiceModel


class ElectionTests(APITestCase, TestMixin):
    def setUp(self):
        self.client = APIClient()
        self.init()
        
    def test_elections(self):
        url = reverse('election-elections')
        response = self.client.get(url, headers=self.headers)
        
        self.assertEqual(response.status_code, 200)
        pars = response.json()
        sps = pars[0]

        idd = sps['id']
        election = sps['name']
        
        self.assertEqual((idd, election), (self.election_null.id, 'Тут наверное что-то есть'))
    
    def test_delete(self):
        url = reverse('election-delete-election')
        data = {'id': self.election_null.id}
        
        response = self.client.post(url, data=data, headers=self.headers)
        self.assertEqual(response.status_code, 200)
        
        elections = ElectionModel.objects.all().count()
        choices = ChoiceModel.objects.filter(election_id=1).count()
        
        self.assertEqual((elections, choices), (0, 0))
        