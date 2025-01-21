from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField('게시물 내용')
    like = models.IntegerField('좋아요 수', default=0)
    clicked = models.BooleanField('체크여부', default=False)
    created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)