from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    """
    A view function that renders the "index.html" template with a list of all Todo objects.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered "index.html" template with the list of tasks as context.
    """
    tasks = Todo.objects.all()
    print(tasks)
    context = {
        'tasks': tasks,
    }
    return render(request, "index.html", context)


def addTask(request):
    """
    Adds a task to the Todo list.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - If the request method is 'POST', it creates a new task with the provided data and redirects to the 'index' page.
    - If the request method is not 'POST', it retrieves all tasks from the Todo list and renders the 'index.html' template with the tasks.

    """
    if request.method == 'POST':
        if request.POST['task']:
            task = request.POST['task']
            Todo.objects.create(task=task)
    return HttpResponseRedirect('/')


def deleteTask(request, pk):
    """
    Deletes a task from the Todo list.

    Parameters:
    - request: The HTTP request object.
    - pk: The primary key of the task to be deleted.

    Returns:
    - If the request method is 'POST', it redirects to the 'index' page.
    - If the request method is not 'POST', it retrieves all tasks from the Todo list and renders the 'index.html' template with the tasks.

    """

    task = get_object_or_404(Todo, pk=pk)
    print(task)
    task.delete()
    return HttpResponseRedirect('/')
