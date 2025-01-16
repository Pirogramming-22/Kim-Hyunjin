from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from apps.developTool.models import DevTool
from django.http import JsonResponse


# Create your views here.
def list(request):
    try:
        sorting_value = request.GET.get('sorting', None)
        ideas = Idea.objects.all()
        if sorting_value == 'starsort':
            ideas = ideas.order_by('-starred')
        elif sorting_value == 'registersort':
            ideas = ideas.order_by('id')
        elif sorting_value == 'recentsort':
            ideas = ideas.order_by('-id')
        elif sorting_value == 'namesort':
            ideas = ideas.order_by('title')
        ctx = {
            'ideas': ideas,
        }
        return render(request, 'idea/list.html', context=ctx)
    except:
        ideas = Idea.objects.all()

    ctx = {
        'ideas': ideas,
    }
    return render(request, 'idea/list.html', context=ctx)

def detail(request, pk):
    target_idea = Idea.objects.get(id=pk)
    ctx = {'idea': target_idea,}
    return render(request, 'idea/detail.html', context=ctx)

def create(request):
    if request.method == 'GET':
        form = IdeaForm()
        ctx = {'form': form}
        return render(request, 'idea/create.html', context=ctx)
    else:
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
        return redirect(f'/ideas/detail/{idea.pk}', idea.pk)

def update(request, pk):
    if request.method == 'GET':
        idea = Idea.objects.get(id=pk)
        form = IdeaForm(instance=idea)
        ctx = {'form': form,
               'pk': pk}

        return render(request, 'idea/update.html', context=ctx)
    else:
        idea = Idea.objects.get(id=pk)
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
        return redirect(f'/ideas/detail/{pk}', pk)

def delete(request, pk):
    idea = Idea.objects.get(id=pk)
    idea.delete()
    return redirect('/ideas')

def check(request, pk):
    try:
        idea = Idea.objects.get(id=pk)
        return JsonResponse({'starred': idea.starred})
    except Idea.DoesNotExist:
        return JsonResponse({'status': False}, status=404)

def change(request, pk):
    if request.method == 'GET':
        idea = Idea.objects.get(id=pk)
        idea.starred = not idea.starred
        #print(idea.starred)
        idea.save()
        return JsonResponse({'status': True})

def add(request, pk):
    idea = Idea.objects.get(id=pk)
    if idea.interest <5:
        idea.interest += 1
        idea.save()
    return JsonResponse({'interest': idea.interest})

def minus(request, pk):
    idea = Idea.objects.get(id=pk)
    if idea.interest >= 0:
        idea.interest -= 1
        idea.save()
    return JsonResponse({'interest': idea.interest})