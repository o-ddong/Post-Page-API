from django.db import models

# Create your models here.
from applications.base.models import BaseModel
from applications.board.models import Post


class User(BaseModel):
    """
    유저 모델
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    password = models.CharField(max_length=30, verbose_name='비밀번호')