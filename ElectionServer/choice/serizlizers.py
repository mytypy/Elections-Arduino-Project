from rest_framework.serializers import ModelSerializer
from .models import ChoiceModel


class ChoicesSerializer(ModelSerializer):
    
    class Meta:
        model = ChoiceModel
        fields = ('id', 'name')