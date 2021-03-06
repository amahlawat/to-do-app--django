from turtle import update
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem2
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem2.objects.all()
    if len(all_todo_items) > 0:
        return render(request, 'todolist.html',
        {'all_items': all_todo_items}) 
    else:
        return render(request, 'todolist.html',
        {'all_items': ['test']})

def addTodoView(request):
    x = request.POST.get('content', False)
    new_item = TodoListItem2(description = x, status = 'in progress')
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem2.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

def editView(request, i):
    y = TodoListItem2.objects.get(id=i)
    print(" y ", y.description)
    return render(request, 'edit.html',
    {'data': { 'idx': i, 'value': y}}) 

def updateTodoItem(request, i):
    updatedData = request.POST.get('updatedData', False)
    TodoListItem2.objects.filter(pk=i).update(description = updatedData)
    return HttpResponseRedirect('/todoapp/')
    
def updateTaskStatus(request, i, checkbox, status):
    print(" checkbox ", checkbox, 'type', type(checkbox), ' status ', status, ' type ', type(status))
    updatedStatus = ''
    if checkbox == 'True':
        updatedStatus = status
    else:    
        updatedStatus = request.POST.get('status', False)
    TodoListItem2.objects.filter(pk=i).update(status = updatedStatus)
    return HttpResponseRedirect('/todoapp/')

