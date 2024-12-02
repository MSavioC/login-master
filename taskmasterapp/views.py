from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task

def login_view(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tarefas/')
        else:
            return render(request, 'login/index.html', {'error': 'Credenciais invalidas'})
    
    
    return render(request, 'login/index.html')

def TaskList_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasklist/tasklist.html", {"tasks": tasks})



def registro_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "As senhas nao coincidem")
            return redirect("registro")
       
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Usuario registrado com sucesso! Faça login.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Erro ao registrar o usuario: {e}")
            return redirect ("registro")
    return render(request, 'registro/cadastrar.html')

def registrotarefas_view(request):
    if request.method == "POST":
        # OBTEM OS DADOS DO FORMULARIO
        title = request.POST.get("title")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")

        #cria a tarefa e associa ao usuario logado
        Task.objects.create(
            user=request.user, #associando ao usuario logado
            title=title,
            due_date=due_date,
            priority=priority,
        )
        return redirect("tarefas")
    return render(request, "taskregister/tasksregister.html")

  