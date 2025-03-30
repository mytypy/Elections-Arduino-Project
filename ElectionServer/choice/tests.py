from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from mixins.test_mixin import TestMixin
from choice.models import ChoiceModel


class ChoiceTest(APITestCase, TestMixin):
    def setUp(self):
        self.client = APIClient()
        self.init()

    def test_add_chococo(self):
        test_yes = {'name': 'МяуМУр', 'election': 1}
        test_no = {'name': 'Нет, не идёт', 'election': 993}
        url = reverse('choice-add-choice')
        
        response1 = self.client.post(url, data=test_yes, headers=self.headers)
        self.assertEqual(response1.status_code, 200)
        
        choice = ChoiceModel.objects.get(name='МяуМУр')

        self.assertEqual(choice.election.id, 1)
        self.assertEqual(choice.name, 'МяуМУр')
        
        response2 = self.client.post(url, data=test_no, headers=self.headers)
        self.assertEqual(response2.status_code, 400)
        
        choice2 = ChoiceModel.objects.filter(name='Нет, не идёт').count()
        self.assertEqual(choice2, 0)