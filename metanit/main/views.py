from django.shortcuts import render, redirect
from .models import File, Files
from .forms import FilesForm, InfoForm


def reg(request):
    error = ''
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            error = 'ERROR'
    else:
        form = InfoForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/reg.html', context)


def home(request):
    files = Files.objects.order_by('-id')
    return render(request, 'main/home.html', {'title': 'Загруженные файлы', 'files': files})


def load(request):
    if request.method == 'POST':
        form = FilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FilesForm()
    context = {
        'form': form,
    }
    return render(request, 'main/load.html', context)


def read(request):
    files = File.objects.order_by('-id')

    return render(request, 'main/read.html', {'file': files})
