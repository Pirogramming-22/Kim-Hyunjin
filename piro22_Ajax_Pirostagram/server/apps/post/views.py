from django.shortcuts import render
from apps.post.models import Post
from django.views.decorators.csrf  import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def main(request):
    sorting_value = request.GET.get('sorting', None)
    posts = Post.objects.all()
    '''if sorting_value == 'starsort':
        ideas = ideas.order_by('-starred')
    elif sorting_value == 'registersort':
        ideas = ideas.order_by('id')
    elif sorting_value == 'recentsort':
        ideas = ideas.order_by('-id')
    elif sorting_value == 'namesort':
        ideas = ideas.order_by('title')'''
    ctx = {
            'posts': posts,
        }
    return render(request, 'post/post.html', ctx)

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    #print(req)
    post_id=int(req["pk"])

    post=Post.objects.get(id=post_id)

    if post.clicked:
        post.like -= 1
        post.clicked = False
    else:
        post.like += 1
        post.clicked = True
    post.save()
    return JsonResponse({'id':post_id, 'like':post.like, 'clicked':post.clicked})
