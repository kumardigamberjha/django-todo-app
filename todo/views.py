from django.shortcuts import render, redirect
from .models import todo

def index(request):
    todos= todo.objects.all()
    # print(todos)
    context= {'todos': todos}
    return render(request, 'todo/index.html', context)

def todolist(request):
    todos= todo(name= request.POST['name'])
    # print(todos)
    todos.save()
    return redirect('/')


def deltodo(request, todo_id):
    todos= todo.objects.get(id=todo_id)
    todos.delete()
    return redirect('/')