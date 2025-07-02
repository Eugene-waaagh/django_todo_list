from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.template import loader
from .forms import TaskForm

def index(request):
    #List of all tasks
    tasks = Task.objects.all()

    return render(request, "todo/index.html", {'tasks': tasks,})

def create_task(request):
    form = TaskForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        form = TaskForm()

    return render(request, "todo/create_task.html", {"form": form})
