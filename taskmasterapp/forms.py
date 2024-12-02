from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']
        widgets ={
            'due_date': forms.DateImput(attrs={'type': 'date'}),
            'priority': forms.Select(),
        }