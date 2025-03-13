from django.http import HttpResponse
from django.shortcuts import render,redirect
from todo.models import Task

def addTask(rqst):
    task = rqst.POST['task']
    Task.objects.create(task = task) # first task ta hoilo models.py er task jeta Task class a create kra hoise
    # return HttpResponse('Hello Gulluuh')
    return redirect('home')