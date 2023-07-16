from django.shortcuts import render, redirect
from .models import File, Files
from .forms import FilesForm, InfoForm
import pandas as pd
import os


def reg(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('load')
    form = InfoForm()
    context = {
        'form': form,
    }
    return render(request, 'main/reg.html', context)


def home(request):
    fi = Files.objects.all()
    files = File.objects.all()
    if fi:
        for dirpath, dirname, filename in os.walk("C:\django\metanit\media\ile"):
            for fil in filename:
                ad = os.path.join(dirpath, fil)
        df = pd.read_excel(ad, header=None)
        mas = df.values
        if files:
            File.objects.all().delete()

        for r in range(2, len(mas)):
            abc = File(num=mas[r][0], city=mas[r][1], reg=mas[r][2], fed_o=mas[r][3], hum=mas[r][4], his=mas[r][5],
                       status=mas[r][6], his_name=mas[r][7])
            abc.save()
        os.remove(ad)
        Files.objects.all().delete()

    files = File.objects.all()
    return render(request, 'main/home.html', {'title': 'Таблица', 'files': files})


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
