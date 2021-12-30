from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from user.models import User


def create_telegram_user(username: str, telegram_id: str):

    """
    creates telegram user
    """
    telegram_id = telegram_id
    username = username
    model = get_user_model()
    is_exist = model.objects.filter(username=username).exists()
    if is_exist is True:
        return Response({'detail': 'username already exist'}, status=status.HTTP_400_BAD_REQUEST)
    model.objects.create(username=username, telegram_id=telegram_id)

    return Response({'detail': 'successful'}, status=status.HTTP_201_CREATED)


def get_telegram_user(username: str, telegram_id: str):
    try:
        user = User.objects.get(username=username, telegram_id=telegram_id)
        return user
    except User.DoesNotExist:
        return None
