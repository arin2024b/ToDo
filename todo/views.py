from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from todo.models import Task

def addTask(rqst):
    task = rqst.POST['task']
    Task.objects.create(task = task) # first task ta hoilo models.py er task jeta Task class a create kra hoise
    # return HttpResponse('Hello Gulluuh')
    return redirect('home')

def mark_as_done(rqst,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True 
    task.save()
    return redirect('home')

def mark_as_undone(rqst,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(rqst,pk):
    get_task = get_object_or_404(Task, pk=pk)
    if rqst.method == 'POST':
        new_task = rqst.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(rqst,'edit_task.html',context)
    
def delete_task(rqst,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')