from django.urls import path
from . import views

urlpatterns = [
     path('',views.todo_list,name="todo_list"),
    path('create',views.create_todo,name="create_todo"),
    path('completed/<int:todo_id>',views.completed_todo,name="completed_todo"),
    path('delete/<int:todo_id>',views.delete_todo,name="delete_todo"),
]