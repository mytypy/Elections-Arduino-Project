from election.models import ElectionModel
from choice.models import ChoiceModel
from models.models import SecretKey


class TestMixin:    
    def create_data(self):
        self.data_null_1 = {
            'id_card': self.id_card,
            'election': self.election_null.id,
            'choice': self.choice_for_null_1.id
            }
        
    def create_elections(self):
        self.election_null = ElectionModel.objects.create(name='Тут наверное что-то есть')
    
    def create_choices(self):
        self.choice_for_null_1 = ChoiceModel.objects.create(name='Yes', election=self.election_null) 
    
    def init(self):
        self.id_card = 'SBX66t96ggzxc'
        secret = SecretKey()
        self.hash = secret.SECRET
        
        self.create_elections()
        self.create_choices()
        self.create_data()
        self.headers = {'Hash': self.hash}