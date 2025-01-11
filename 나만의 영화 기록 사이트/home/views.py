from django.shortcuts import render
from reviews.models import Review

def main(request):
  reviews = Review.objects.all()
  context = {'reviews' :reviews}
  return render(request, 'home/home.html', context)
