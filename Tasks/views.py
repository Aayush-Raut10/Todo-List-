from django.shortcuts import render, redirect
from django.http import HttpResponse
from Tasks.models import Tasks

# Create your views here.
def index(request):
    
    if request.method == "POST":

        task = request.POST.get("title")

        newTask = Tasks(title=task)
        newTask.save()

        return redirect('index')   

    else:

        tasks = Tasks.objects.all()

        context = {
            "tasks":tasks,
        }
    return render(request, "Tasks/index.html", context=context)

def delete_task(request, pk):

    try:
        task = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        pass
    
    task.delete()

    return redirect('index')



def edit_task(request,pk):

    task = Tasks.objects.get(id=pk)

    if request.method == "POST":

        #get new title from form
        new_title = request.POST.get("title")

        task.title = new_title

        task.save()

        return redirect('index')
    
    else:

        return render(request, "Tasks/edit.html",{'task':task})