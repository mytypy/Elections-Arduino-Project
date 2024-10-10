from rest_framework.serializers import ModelSerializer
from choice.serizlizers import ChoicesSerializer
from .models import ElectionModel


class ElectionSerializer(ModelSerializer):
    choice = ChoicesSerializer(many=True, read_only=True)
    
    
    class Meta:
        model = ElectionModel
        fields = ('id', 'name', 'choice', 'date_created')