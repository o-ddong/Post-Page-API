from django.db import models

# Create your models here.
from application.base.models import BaseModel
from application.board.models import Post


class User(BaseModel):
    """
    유저 모델
    """
    id = models.IntegerField(primary_key=True)
    password = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='비밀번호')
