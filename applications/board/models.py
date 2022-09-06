from django.db import models

# Create your models here.
from applications.base.models import BaseModel

class Post(BaseModel):
    """
    게시글 모델
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name='제목')
    content = models.CharField(max_length=200, verbose_name='본문')

    def __str__(self):
        return str(self.id)
