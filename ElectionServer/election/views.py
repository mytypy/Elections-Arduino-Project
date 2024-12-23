from typing import Any

from django.http import HttpRequest, QueryDict
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from choice.models import ChoiceModel
from main.models import UserModel
from .models import ElectionModel
from .serializers import ElectionSerializer


class ElectionModelView(ModelViewSet):
    queryset = ElectionModel.objects.all()
    serializer_class = ElectionSerializer
    
    @action(
        methods=['GET'],
        detail=False
    )
    def get_election(self, request: HttpRequest) -> Response:
        get_data: dict = request.GET
        
        try:
            election: ElectionModel = ElectionModel.objects.get(pk=get_data['id'])
            choices: ChoiceModel = election.choices.all()
        except Exception as er:
            return Response({'response': er.args[0]})
        
        data: dict = {
            'election': {
                'id': election.id,
                'name': election.name,
                'created': election.date_created.date()
            },
            'choices': [{'id': i.id, 'name': i.name} for i in choices]
            
        }
        
        return Response({'response': data})

    @action(
        methods=['DELETE'],
        detail=False
    )
    def delete_election(self, request: HttpRequest) -> Response:
        '''{
method: 'DELETE',
body: {
    "id": num
    },
headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
}'''
        data: str = request.body.decode('utf-8')
        result: dict[Any, Any | list] = QueryDict(data).dict()

        election: int = result['id']
        
        try:
            ElectionModel.objects.get(pk=election).delete()
        except Exception as er:
            return Response({'response': er.args[0]})
        
        return Response({'response': 'Удаление прошло успешно! Все участники, выборы к голосованию и голосование, были удалены из базы данных'})

    @action(
        methods=['GET'],
        detail=False
    )
    def finish_election(self, request: HttpRequest) -> Response:
        election_id: dict = request.GET
        
        try:
            data_votes: list = list(ChoiceModel.objects.filter(election_id=election_id['id']).values('name').annotate(votes=Count('user')))
            peoples_count: int = UserModel.objects.filter(election_id=election_id['id']).count()
            
            print(peoples_count)
        except Exception as er:
            return Response({'response': f'Что-то пошло не так, либо неправильный id, либо вы его вообще не передали :/. Ошибка {er}'})
                
        statistic: dict = dict(map(lambda k: (k['name'], round(k['votes']/peoples_count * 100)), data_votes))
        winner = max(statistic, key=lambda x: statistic[x])

        data = {
            'message': 'Итоги голосования',
            'statistic': [f'За ответ {name} проголосовало {value}%' for name, value in statistic.items()],
            'winner': f'Победил выбор "{winner}" с процентом голосов {statistic[winner]}%'
        }
        return Response({'response': data})

    @action(
        methods=['POST'],
        detail=False
    )
    def add_election(self, request: HttpRequest) -> Response:
        data: dict = request.POST

        election_name: str = data['name']
        
        election = ElectionModel.objects.filter(name=election_name)
        
        if election.exists():
            return Response({'response': f'"{election_name}", уже существует в базе данных'})

        try:
            ElectionModel.objects.create(name=election_name).save()
        except Exception as er:
            return Response({'response': f'Error {er.args[0]}'})
        
        return Response({'response': 'Голосование добавлено'})