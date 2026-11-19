from django.shortcuts import render, redirect
from .models import Task
from datetime import datetime


def lista(request): #lista_de_tarefas.html
    tarefas = Task.objects.all()
    return render(request, "lista_de_tarefas.html", {"tasks": tarefas})

# def task_list(request):
#     tasks = Task.objects.all()  # pega todas as tarefas
#     return render(request, "task_list.html", {"tasks": tasks})


def create(request):
    if request.method == "POST":
        title = request.POST['title']
        descricao = request.POST['descricao']
        status = request.POST["status"]
        prazo = request.POST["prazo"]

        prazo = datetime.strptime(prazo, "%Y-%m-%dT%H:%M")

        Task.objects.create(
            title=title,
            descricao=descricao,
            prazo=prazo,
            status=status
        )
        return redirect('lista_de_tarefas')
    
    return render(request, 'form_add.html')


def update(request, pk):
    tarefa = Task.objects.get(pk=pk)
    if request.method == 'POST':
        tarefa.title = request.POST["title"]
        tarefa.descricao = request.POST["descricao"]
        tarefa.status = request.POST["status"]
        prazo = request.POST["prazo"]
        tarefa.prazo = datetime.strptime(prazo, "%Y-%m-%dT%H:%M")

        tarefa.save()
        return redirect('lista_de_tarefas')
    return render(request, 'form_add.html', {'tarefa': tarefa}) #analisar em caso de erro


def delete(request,pk):
    tarefa = Task.objects.get(pk = pk)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('lista_de_tarefas')
    return render (request,'deletar.html',{'task':tarefa}) 

# def note_delete(request,pk):
#     note = Note.objects.get(pk = pk)
#     if request.method == 'POST':
#         note.delete()
#         return redirect('note_list')
#     return render (request,'note/note_confirm_delete.html',{'note':note})


# Create your views here.
