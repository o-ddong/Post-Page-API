from django.db import models

# Create your models here.
from applications.base.models import BaseModel
from applications.board.models import Post


class User(BaseModel):
    """
    유저 모델
    """
    id = models.IntegerField(primary_key=True)
    password = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='비밀번호')