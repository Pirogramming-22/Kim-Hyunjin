from django.db import models

class DevTool(models.Model):
    name = models.CharField('이름',max_length=30, default='')
    kind = models.CharField('종류',max_length=40, default='')
    content = models.TextField('내용', default='')

    def __str__(self):
        return self.name