from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel


class User(AbstractUser, BaseModel):

    telegram_id = models.CharField(max_length=128, null=True)
