from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('todo_title', 'todo_description')
        widgets = {
        'todo_description': forms.Textarea(attrs={'rows':4, 'cols':190}),
        }

    