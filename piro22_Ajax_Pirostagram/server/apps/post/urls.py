from django.urls import path
from apps.post import views

app_name = 'post'

urlpatterns = [
    path('', views.main, name='main'),
    path('like/', views.like, name='like'),
    ]