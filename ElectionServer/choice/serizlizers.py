from rest_framework import serializers
from .models import ChoiceModel


class ChoicesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChoiceModel
        fields = ('name', 'election')
        
    def validate_name(self, value):
        choice = ChoiceModel.objects.filter(name=value).exists()
        
        if choice:
            raise serializers.ValidationError('Выбор с таким именем уже существует!')
        
        return value
    
    def create(self, validated_data):
        return ChoiceModel.objects.create(**validated_data)