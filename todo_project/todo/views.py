from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .form import TodoForm


# Create your views here.
class TodoList(CreateView):
    form_class = TodoForm
    template_name = 'todo.html'

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Todo.objects.order_by('id')
        return super(TodoList, self).get_context_data(**kwargs)


class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')