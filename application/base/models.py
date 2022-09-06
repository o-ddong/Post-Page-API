from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    공통 모델
    """
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        abstract = True