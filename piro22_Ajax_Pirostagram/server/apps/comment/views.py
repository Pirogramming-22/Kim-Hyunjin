from django.shortcuts import render, redirect
from apps.comment.models import Comment
from apps.post.models import Post
from django.views.decorators.csrf  import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def main(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    ctx = {
        'postid' : pk,
        'comments': comments,
    }
    return render(request, 'comment/list.html', ctx)

@csrf_exempt
def create_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get("post_id")
        text = data.get("text")

        try:
            post = Post.objects.get(id=post_id)

            comment = Comment.objects.create(post=post, content=text)
            return JsonResponse({
                "id": comment.id,
                "content": comment.content,
            }, status=201)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)

    return JsonResponse({"error": "Invalid request method"}, status=400)

def delete(request, pk, post_id):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect(f'/comments/{post_id}')

@csrf_exempt
def like(request):
    req = json.loads(request.body)
    #print(req)
    comment_id = int(req["pk"])

    comment = Comment.objects.get(id=comment_id)
    #print(comment.like)

    if comment.clicked:
        comment.like -= 1
        comment.clicked = False
    else:
        comment.like += 1
        comment.clicked = True
    comment.save()
    #print({'id':comment_id, 'like':comment.like, 'clicked':comment.clicked})
    return JsonResponse({'id':comment_id, 'like':comment.like, 'clicked':comment.clicked})