from django.urls import path
from apps.idea import views

app_name = 'idea'

urlpatterns = [
    path('ideas/', views.list, name='list'),
    path('ideas/detail/<int:pk>', views.detail, name='detail'),
    path('ideas/create', views.create, name='create'),
    path('ideas/update/<int:pk>', views.update, name='update'),
    path('ideas/delete/<int:pk>', views.delete, name='delete'),
    path('ideas/check/<int:pk>', views.check, name='check'),
    path('ideas/change/<int:pk>', views.change, name='change'),
    path('ideas/add/<int:pk>', views.add, name='add'),
    path('ideas/minus/<int:pk>', views.minus, name='minus'),
    ]