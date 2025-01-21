from django.db import models
from django.db.models import ForeignKey
from apps.post.models import Post

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField('댓글 내용')
    like = models.IntegerField('좋아요 수', default=0)
    clicked = models.BooleanField('체크여부', default=False)
    created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)