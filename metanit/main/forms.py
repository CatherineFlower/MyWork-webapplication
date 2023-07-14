from .models import File
from django.forms import ModelForm, TextInput, Textarea, FileInput

"""class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),
        }
"""


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ["title", "file"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введите название"
            }),
            "file": FileInput()
        }
