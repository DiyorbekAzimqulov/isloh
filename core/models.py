from django.db import models
from uuid import uuid4
# Create your models here.


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid4)
    created_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
