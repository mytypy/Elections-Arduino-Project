from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import ElectionModel, UserModel, ChoiceModel
from .serializers import ElectionSerializer, UserSerializer


class ElectionModelView(ModelViewSet):
    queryset = ... # Доделать


class UserModelView(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def post_user_election(self, request: HttpRequest) -> Response:
        data = request.POST
        
        id_card = data['id_card']
        election = data['election'][0]
        choice = data['choice'][0]
        
        user = UserModel.objects.filter(id_card=id_card)
        
        if user.exists():
            user_election = user[0].election.name
            return Response({'response': f'Пользователь уже учавствует в голосовании "{user_election}"'})

        try:
            election = ElectionModel.objects.get(pk=election)
            choice = ChoiceModel.objects.get(pk=choice)
            
            UserModel.objects.create(id_card=id_card, election=election, choice=choice).save()
        except Exception as er:
            return Response({'error': er.args[0]})
        
        return Response({'response': 'Запись добавлена'})