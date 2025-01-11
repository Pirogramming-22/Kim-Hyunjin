from django.urls import path
from .views import *

app_name = 'reviews'

urlpatterns = [
  #리뷰 작성
  path('create', review_create, name='review_create'),
  #리뷰 내용 보기
  path('detail/<int:pk>', review_detail, name='review_detail'),
  #리뷰 수정
  path('update/<int:pk>', review_update, name='review_update'),
  #리뷰 삭제
  path('delete/<int:pk>', review_delete, name='review_delete'),
]