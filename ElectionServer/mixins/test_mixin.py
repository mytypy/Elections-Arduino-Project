import os
from election.models import ElectionModel
from choice.models import ChoiceModel
from main.models import Hash


class TestMixin:    
    def create_data(self):
        self.data_null_1 = {'id_card': self.id_card, 'election': 1, 'choice': 1}
        
    def create_elections(self):
        self.election_null = ElectionModel.objects.create(pk=1, name='Тут наверное что-то есть')
    
    def create_choices(self):
        self.choice_for_null_1 = ChoiceModel.objects.create(pk=1, name='Yes', election=self.election_null) 
    
    def init(self):
        self.id_card = 'SBX66t96ggzxc'
        self.hash = os.environ.get('HASH_ELECTION')
        self.sha256_hash = os.environ.get('SHA_ELECTION') # Символы ``, нужно экранировать вот так \`\`(Только на linux)
        Hash.objects.create(pk=1, password=self.sha256_hash) 
        
        self.create_elections()
        self.create_choices()
        self.create_data()
        self.headers = {'Hash': self.hash}