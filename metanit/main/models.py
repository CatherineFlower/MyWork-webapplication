from django.db import models
import pandas as pd
import pretty_html_table as pht


class Info(models.Model):
    email = models.EmailField('Email')
    name = models.CharField('ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь сайта'
        verbose_name_plural = 'Пользователи сайта'


class Files(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='file/%Y-%m-%d/')

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.title, self.file)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class File(models.Model):
    title = 1
