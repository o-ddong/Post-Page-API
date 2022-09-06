from django.db import models

# Create your models here.
from application.base.models import BaseModel

class Post(BaseModel):
    """
    게시글 모델
    """
    title = models.CharField(max_length=20, verbose_name='제목')
    content = models.CharField(max_length=200, verbose_name='본문')

