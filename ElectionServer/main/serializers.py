from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ('id_card', 'election', 'choice')
        
    def validate_id_card(self, value):
        user = UserModel.objects.filter(id_card=value)
        
        if user:
            raise serializers.ValidationError('Этот пользователь уже голосовал')
        
        return value

    def create(self, validated_data):
        return UserModel.objects.create(**validated_data)