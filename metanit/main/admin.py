from django.contrib import admin
from .models import Files, Info, File


admin.site.register(Files)
admin.site.register(File)
admin.site.register(Info)