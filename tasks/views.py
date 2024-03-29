from django.shortcuts import render
from tasks.models import *
from django.views.generic.edit import CreateView
from tasks.forms import *

#def index(request):
 #   return render(request, 'tasks/base.html')


class CreateTaskForm(CreateView):
    model = TaskModel
    form_class = TaskCreateForm
    template_name = 'tasks/create_task.html'
    
