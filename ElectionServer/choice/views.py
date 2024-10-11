from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from choice.models import ChoiceModel
from election.models import ElectionModel
from .serizlizers import ChoicesSerializer


class ChoiceViewSet(ModelViewSet):
    queryset = ChoiceModel.objects.all()
    serializer_class = ChoicesSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def add_choice(self, request: HttpRequest) -> Response:
        data: dict = request.POST
        
        name: str = data['name']
        election: str = data['election']

        try:
            election: ElectionModel = ElectionModel.objects.get(pk=election)
            ChoiceModel.objects.create(name=name, election=election).save()
        except Exception as er:
            return Response({'response': f'Error {er.args[0]}'})
        
        
        return Response({'response': 'Действие добавлено в базу данных'})