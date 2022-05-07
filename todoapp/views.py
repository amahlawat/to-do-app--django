from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoListItem
from django.http import HttpResponseRedirect

# Create your views here.
def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items': all_todo_items}) 

def addTodoView(request):
    x = request.POST.get('content', False)
    new_item = TodoListItem(content = x)
    print(" new_item ", new_item)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')

def editView(request, i):
    y = TodoListItem.objects.get(id=i)
    return render(request, 'edit.html',
    {'data': y}) 
