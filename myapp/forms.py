from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'

        labels = {'todo':'Enter Your todos...'}

        widgets = {
            'todo':forms.TextInput(attrs = {'class':'form-control'})
        }