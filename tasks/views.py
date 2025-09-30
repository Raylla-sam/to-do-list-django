from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.contrib.auth.decorators import login_required


@login_required
def lista(request):
    tarefas = Task.objects.filter(user=request.user)  
    return render(request, "lista_de_tarefas.html", {"tasks": tarefas})

# def task_list(request):
#     tasks = Task.objects.all()  # pega todas as tarefas
#     return render(request, "task_list.html", {"tasks": tasks})


@login_required
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        descricao = request.POST['descricao']
        status = request.POST["status"]
        prazo = request.POST["prazo"]

        prazo = datetime.strptime(prazo, "%Y-%m-%dT%H:%M")

        Task.objects.create(
            user=request.user,   
            title=title,
            descricao=descricao,
            prazo=prazo,
            status=status
        )
        return redirect('lista_de_tarefas')
    
    return render(request, 'form_add.html')



@login_required
def update(request, pk):
    tarefa = Task.objects.get(pk=pk, user=request.user)  
    if request.method == 'POST':
        tarefa.title = request.POST["title"]
        tarefa.descricao = request.POST["descricao"]
        tarefa.status = request.POST["status"]
        prazo = request.POST["prazo"]
        tarefa.prazo = datetime.strptime(prazo, "%Y-%m-%dT%H:%M")

        tarefa.save()
        return redirect('lista_de_tarefas')
    return render(request, 'form_add.html', {'tarefa': tarefa})


@login_required
def delete(request, pk):
    tarefa = Task.objects.get(pk=pk, user=request.user)  
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_de_tarefas')
    return render(request, 'deletar.html', {'task': tarefa})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, f'Conta criada para {username}! Faça login agora.')
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'tela_login.html' 
    authentication_form = CustomLoginForm  

# Create your views here.
