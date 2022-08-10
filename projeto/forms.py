from django import forms

from .models import Vaga


class TaskForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'requisitos', 'salario', 'escolaridade']
        
