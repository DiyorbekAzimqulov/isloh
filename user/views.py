from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from authentication.authentication import TelegramBotAuthentication, TelegramUserAuthentication
from .serializers import TelegramUserSerializer
from .services.regisration import create_telegram_user, get_telegram_user


class TelegramUserView(APIView):
    """
    manages telegram user
    """
    authentication_classes = (TelegramBotAuthentication, )

    def post(self, request):
        """
        creates telegram user and saves it in the database
        """
        serializer = TelegramUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return create_telegram_user(**serializer.validated_data)


class RetrieveTelegramUser(RetrieveAPIView):
    authentication_classes = (TelegramUserAuthentication, )
    serializer_class = TelegramUserSerializer

    def get_object(self):
        return self.request.user
