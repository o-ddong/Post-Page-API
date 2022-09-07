from django.db import models

# Create your models here.

class Post(models.Model):
    """
    게시글 모델
    """
    title = models.CharField(max_length=20, verbose_name='제목')
    content = models.CharField(max_length=200, verbose_name='본문')
    password = models.CharField(max_length=20, verbose_name="비밀번호 여부")
    weather = models.CharField(max_length=20, null=True, verbose_name="현재 날씨")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    def __str__(self):
        return str(self.id)
