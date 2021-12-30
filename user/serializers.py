from rest_framework import serializers
from user.models import User


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'telegram_id',
            'username'
        ]
