from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(rqst):
    # return HttpResponse('<h1><b>Home Page</b></h1>')
    tasks = Task.objects.filter(is_completed = False).order_by('-updated_at') # ekhne updated_at er age - daoar reason hoilo descending order a list ta home page a show krano
    context = {
        'tasks' : tasks,
    }
    return render(rqst,'home.html',context)