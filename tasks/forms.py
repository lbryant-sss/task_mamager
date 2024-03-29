
from django import forms
from .models import TaskModel

class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'  # Include all fields from the Task model
