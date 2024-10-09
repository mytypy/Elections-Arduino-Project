from typing import Any
from django.http import HttpRequest, QueryDict
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import ElectionModel, UserModel, ChoiceModel
from .serializers import ElectionSerializer, UserSerializer


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
            peoples_count: int = sum(map(lambda x: x['votes'], data_votes))
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
        

class UserModelView(ModelViewSet):
    queryset: UserModel = UserModel.objects.all()
    serializer_class: UserSerializer = UserSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def post_user_election(self, request: HttpRequest) -> Response:
        data: dict = request.POST
                
        id_card: str = data['id_card']
        election: str = data['election'][0]
        choice: str = data['choice'][0]
        
        user: UserModel = UserModel.objects.select_related('election').filter(id_card=id_card).first()
                
        if user:
            if user.election.id == int(election):
                return Response({'response': f'Пользователь уже учавствует в этом голосовании "{user.election.name}"'})

        try:
            election: ElectionModel = ElectionModel.objects.get(pk=election)
            choice: ChoiceModel = ChoiceModel.objects.get(pk=choice)
            
            UserModel.objects.create(id_card=id_card, election=election, choice=choice).save()
        except Exception as er:
            return Response({'response': er.args[0]})
        
        return Response({'response': 'Запись добавлена'})