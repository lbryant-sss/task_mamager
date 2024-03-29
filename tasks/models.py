from django.db import models
from django.contrib.auth.models import User

class TaskModel(models.Model):
    STATUS_CHOICES = (
        ('todo', 'To Do'),
        ('in_progress', 'In Prgress'),
        ('compete', 'Completed')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
