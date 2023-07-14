from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm


def home(request):
    #tasks = Task.objects.order_by('-id')
    #files = File.objects.order_by('-id')[:1]
    files = File.objects.all()
    return render(request, 'main/home.html', {'title': 'Загруженные файлы', 'files': files})


"""def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'иди нафиг, пиши нормально'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)"""


def load(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
    context = {
        'form': form,
    }
    return render(request, 'main/load.html', context)
