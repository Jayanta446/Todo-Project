from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name = 'add_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name = 'delete_todo')
]
