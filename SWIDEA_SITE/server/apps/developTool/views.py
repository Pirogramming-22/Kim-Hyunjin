from django.shortcuts import render, redirect
from .models import DevTool
from .forms import DevToolForm
from apps.idea.models import Idea

def list(request):
    try:
        devtools = DevTool.objects.all()

        #search_txt = request.GET.get("search_txt")
        #min_price = request.GET.get("min_price")
        #max_price = request.GET.get("max_price")

        #posts = Post.objects.filter(title__contains=search_txt, price__range=(min_price, max_price))

    except:
        devtools = DevTool.objects.all()

    ctx = {
        'devtools': devtools,
    }
    return render(request, 'devtool/list.html', context=ctx)

def create(request):
    if request.method == 'GET':
        form = DevToolForm()
        ctx = {'form': form}
        return render(request, 'devtool/create.html', context=ctx)
    else:
        form = DevToolForm(request.POST, request.FILES)
        if form.is_valid():
            devtool = form.save()
        return redirect(f'/devtools/detail/{devtool.pk}', devtool.pk)

def detail(request, pk):
    target_devtool = DevTool.objects.get(id=pk)
    ideas = Idea.objects.filter(devtool=target_devtool)
    ctx = {'devtool': target_devtool,
           'ideas': ideas}
    return render(request, 'devtool/detail.html', context=ctx)

def update(request, pk):
    if request.method == 'GET':
        devtool = DevTool.objects.get(id=pk)
        form = DevToolForm(instance=devtool)
        ctx = {'form': form,
               'pk': pk}

        return render(request, 'devtool/update.html', context=ctx)
    else:
        devtool = DevTool.objects.get(id=pk)
        form = DevToolForm(request.POST, request.FILES, instance=devtool)
        if form.is_valid():
            form.save()
        return redirect(f'/devtools/detail/{pk}', pk)

def delete(request, pk):
    devtool = DevTool.objects.get(id=pk)
    devtool.delete()
    return redirect('/devtools/')