from rest_framework.serializers import ModelSerializer
from .models import ElectionModel


class ElectionSerializer(ModelSerializer):
    
    class Meta:
        model = ElectionModel
        fields = ('id', 'name')