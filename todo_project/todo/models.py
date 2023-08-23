from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class Todo(models.Model):
    todo_title = models.CharField( max_length=50)
    todo_description = models.TextField()

    def __str__(self):
        return self.todo_title

    def get_absolute_url(self):
        return reverse_lazy('todo_list')
    