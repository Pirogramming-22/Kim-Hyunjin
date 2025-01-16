from django.urls import path
from apps.developTool import views

app_name = 'developTool'

urlpatterns = [
    path('devtools/', views.list, name='list'),
    path('devtools/detail/<int:pk>', views.detail, name='detail'),
    path('devtools/create', views.create, name='create'),
    path('devtools/update/<int:pk>', views.update, name='update'),
    path('devtools/delete/<int:pk>', views.delete, name='delete'),
]