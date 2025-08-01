from rest_framework import serializers
from choice.serizlizers import ChoicesSerializer
from .models import ElectionModel
from main.error import HttpError


class ElectionSerializerId(serializers.Serializer):
    id = serializers.IntegerField()
        
    def validate_id(self, value):
        election = ElectionModel.objects.filter(id=value)
        if not election:
            raise serializers.ValidationError('Голосование с таким id не найдено')
        
        return election
    

class ElectionSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only=True)  # поле, связанное с выбором

    class Meta:
        model = ElectionModel
        fields = ('id', 'name', 'date_created', 'choices')


class CreateElectionSerializer(serializers.Serializer):
    name = serializers.CharField()
    
    def validate_name(self, value):
        election = ElectionModel.objects.filter(name=value).exists()
        
        if election:
            raise serializers.ValidationError(f'Голосование "{value}" уже существует!')
        
        return value
    
    def create(self, validated_data):
        return ElectionModel.objects.create(**validated_data)