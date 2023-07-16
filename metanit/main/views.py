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
            for i in range(2, len(mas)):
                id = i - 1
                prov = {"num": mas[i][0], "city": mas[i][1], "reg": mas[i][2], "fed_o": mas[i][3], "hum": mas[i][4],
                        "his": mas[i][5], "status": mas[i][6], "his_name": mas[i][7]}
                stro = File.objects.update_or_create(id=id, defaults=prov)
        else:
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
