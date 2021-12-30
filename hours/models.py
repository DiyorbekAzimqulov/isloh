from django.db import models
from core.models import BaseModel
from django.conf import settings
# Create your models here.


class Category(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128)


class HoursCategory(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    activity_in_minutes = models.IntegerField(null=True)
