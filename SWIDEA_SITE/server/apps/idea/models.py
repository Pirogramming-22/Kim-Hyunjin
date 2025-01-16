from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.developTool.models import DevTool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명',max_length=100)
    image = models.ImageField(upload_to='idea/%Y%m%d', blank=True)
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0, validators=[MinValueValidator(0),MaxValueValidator(5)])
    devtool = models.ForeignKey( DevTool, verbose_name='예상 개발툴', on_delete=models.CASCADE)
    starred = models.BooleanField(default=False)
    created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)