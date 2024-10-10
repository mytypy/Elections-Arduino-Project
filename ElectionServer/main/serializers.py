from rest_framework.serializers import ModelSerializer
from .models import UserModel


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ('id', 'id_card', 'election', 'choice')