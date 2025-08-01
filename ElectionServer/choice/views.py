from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .serizlizers import ChoicesSerializer


class ChoiceViewSet(ViewSet):
    serializer_class = ChoicesSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def add_choice(self, request: HttpRequest) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'response': 'Действие добавлено в базу данных'})