from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .serializers import UserSerializer


class UserViewSet(ViewSet):
    serializer_class = UserSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def post_user_election(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'response': 'Ваш голос учтён'})