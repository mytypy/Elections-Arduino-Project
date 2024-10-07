from rest_framework.serializers import ModelSerializer
from .models import ElectionModel, UserModel


class ElectionSerializer(ModelSerializer):
    
    class Meta:
        model = ElectionModel
        fields = ('id', 'name')


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ('id', 'id_card', 'election', 'choice')