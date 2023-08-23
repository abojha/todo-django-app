from django.urls import path
from .views import TodoList, TodoDelete


urlpatterns = [
    path('', TodoList.as_view(), name='todo_list'),
    path('<int:pk>/delete/', TodoDelete.as_view(), name='todo_delete')
]
