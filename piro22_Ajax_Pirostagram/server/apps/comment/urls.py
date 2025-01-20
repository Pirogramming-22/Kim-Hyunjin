from django.urls import path
from apps.comment import views

app_name = 'comment'

urlpatterns = [
    path('comments/<int:pk>', views.main, name='main'),
    path('comments/like/', views.like, name='like'),
    path('create-comment/', views.create_comment, name='create_comment'),
    path('comments/delete/<int:pk>/<int:post_id>', views.delete, name='delete'),
    ]