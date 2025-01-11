from django.db import models

#Review 모델
class Review(models.Model):
  title = models.CharField(max_length=200)
  created_at = models.DateField()
  genre = models.CharField(max_length=50)
  rate = models.FloatField(default=5.0)
  running_time = models.TextField(default=0)
  content = models.TextField()
  director = models.CharField(max_length=100)
  actor = models.CharField(max_length=100)
  written_at = models.DateTimeField(auto_now=True)