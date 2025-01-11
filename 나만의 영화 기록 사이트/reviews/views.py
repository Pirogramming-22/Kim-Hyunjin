from django.urls import reverse
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def review_create(request):
  if request.method == 'POST':
    review = Review.objects.create(
      title = request.POST['title'],
      created_at = request.POST['created_at'],
      genre = request.POST['genre'],
      rate = request.POST['rate'],
      running_time = request.POST['running_time'], #해결해야함
      content = request.POST['content'],
      director = request.POST['director'],
      actor = request.POST['actor'],
    )
    return redirect("home:main")
  return render(request,'reviews/create.html')


def review_detail(request, pk):
  reviews = Review.objects.get(id=pk)
  time = int(reviews.running_time)//60
  minute = int(reviews.running_time)%60
  context={
    'review' :reviews,
    'time' :time,
    'minute' :minute
  }
  return render(request, 'reviews/detail.html', context)

def review_list(request):
    reviews = Review.objects.all()
    context = {'reviews' :reviews}
    return render(request, 'home.html', context)


def review_update(request, pk):
    review = Review.objects.get(id=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        created_at = request.POST.get('created_at')
        genre = request.POST.get('genre')
        rate = request.POST.get('rate')
        running_time = request.POST.get('running_time')
        content = request.POST.get('content')
        director = request.POST.get('director')
        actor = request.POST.get('actor')
        
        review.title = title
        review.genre = genre
        review.rate = rate
        review.running_time = running_time
        review.content = content
        review.director = director
        review.actor = actor
        review.save()
        return redirect('reviews:review_detail', pk=review.pk)

    context = {'review': review}
    return render(request, 'reviews/update.html', context)

  
def review_delete(request, pk):
  if request.method == 'POST':
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect("home:main")
  return redirect('home:main')