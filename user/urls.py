from django.urls import path
from .views import TelegramUserView, RetrieveTelegramUser

app_name = 'user'
urlpatterns = [
    path('create_telegram_user/', TelegramUserView.as_view(), name='telegram-user'),
    path('get_telegram_user/', RetrieveTelegramUser.as_view(), name='get_telegram_user')
]
