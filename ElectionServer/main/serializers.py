from rest_framework.serializers import ModelSerializer
from .models import ElectionModel, UserModel, ChoiceModel


class ChoicesSerializer(ModelSerializer):
    
    class Meta:
        model = ChoiceModel
        fields = ('id', 'name')


class ElectionSerializer(ModelSerializer):
    choice = ChoicesSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = ElectionModel
        fields = ('id', 'name', 'choice', 'date_created')


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ('id', 'id_card', 'election', 'choice')