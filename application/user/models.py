from django.db import models

# Create your models here.
from application.base.models import BaseModel

class User(BaseModel):
    """
    유저 모델
    """
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=20, verbose_name='비밀번호')
    