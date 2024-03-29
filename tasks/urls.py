from django.urls import path
from tasks.views import *

urlpatterns = [
    #path('', views.index, name='index'),
    path('', CreateTaskForm.as_view()),
]