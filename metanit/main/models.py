from django.db import models


class Info(models.Model):
    email = models.EmailField(verbose_name='Email')
    name = models.CharField(verbose_name='ФИО')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь сайта'
        verbose_name_plural = 'Пользователи сайта'


class Files(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='ile/')

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.title, self.file)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class File(models.Model):
    num = models.CharField(verbose_name='№', default='-')
    city = models.CharField(verbose_name='Город', default='-')
    reg = models.CharField(verbose_name='Регион', default='-')
    fed_o = models.CharField(verbose_name='Федеральный округ', default='-')
    hum = models.CharField(verbose_name='Население', default='-')
    his = models.CharField(verbose_name='Основание или первое упоминание', default='-')
    status = models.CharField(verbose_name='Статус города', default='-')
    his_name = models.CharField(verbose_name='Прежние названия', default='-')

    def __str__(self):
        return self.num

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Расшифровка файла'
