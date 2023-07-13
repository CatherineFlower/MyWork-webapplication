from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class File(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='file/%Y-%m-%d/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
