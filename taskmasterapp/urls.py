from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),

    path('taskregister/', views.registrotarefas_view, name='tasksregister'),

    path('registro/', views.registro_view, name='registro'),

    path('tarefas/', views.TaskList_view, name='tarefas'),
]
