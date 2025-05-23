
from django.shortcuts import render, redirect

from .models import Task

from .forms import TaskForm


def task_list(request):

    tasks = Task.objects.all()

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def task_create(request):

    form = TaskForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})


def task_update(request, pk):

    task = Task.objects.get(id=pk)

    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():

        form.save()

        return redirect('task_list')

    return render(request, 'tasks/task_form.html', {'form': form})


def task_delete(request, pk):

    task = Task.objects.get(id=pk)

    if request.method == "POST":

        task.delete()

        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})