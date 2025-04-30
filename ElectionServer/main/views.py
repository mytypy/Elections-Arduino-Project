import json


from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import UserModel
from choice.models import ChoiceModel
from .serializers import UserSerializer
from election.models import ElectionModel
from .errors import ERRORS

        
class UserModelView(ModelViewSet):
    queryset: UserModel = UserModel.objects.all()
    serializer_class: UserSerializer = UserSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def post_user_election(self, request: HttpRequest) -> Response:
        try:
            data: dict = json.loads(request.body)
        except Exception:
            return Response({'response': 'Ошибка десереализации. Возможно вы не корректно передали JSON'}, status=500)

        id_card: str = data['id_card']
        election: str = data['election']
        choice: str = data['choice']
        
        user: UserModel = UserModel.objects.select_related('election').filter(id_card=id_card).first()
                
        if user:
            if user.election.id == int(election):
                return Response({'response': f'Пользователь уже учавствует в этом голосовании "{user.election.name}"'}, status=400)
                
        try:
            election: ElectionModel = ElectionModel.objects.get(pk=election)
            choice: ChoiceModel = ChoiceModel.objects.filter(pk=choice, election=election)[0]
            UserModel.objects.create(id_card=id_card, election=election, choice=choice).save()
        except Exception as er:
            main_error = er.args[0].split()
            stringa = ERRORS.get(main_error[0], 'У вас неправильные данные. Проверьте их корректность, либо позовите администратора')
            return Response({'response': stringa}, status=400)
            
        return Response({'response': 'Запись добавлена'})

    @action(
        methods=['GET'],
        detail=False
    )
    def get_user(self, request: HttpRequest) -> Response:
        data: dict = request.GET
        
        user_card_id: str | None = data.get('card_id')
        
        try:
            user: UserModel = UserModel.objects.select_related('election').select_related('choice').get(pk=user_card_id)
        except Exception:
            return Response({'response': 'Такого пользователя не существует или вы не передали параметр'}, status=400)
        
        data_user = {
            'card_id': user.id_card,
            'election': user.election.name,
            'choice': user.choice.name
        }
        
        return Response({'response': {'user_info': data_user}})
