from django.shortcuts import render, redirect
from django.http import HttpResponse
from Tasks.models import Tasks

# Create your views here.
def index(request):

    if not request.session.session_key:
        request.session.create()
    
    if request.method == "POST":

        task_title = request.POST.get("title")

        if task_title:

            newTask = Tasks(title=task_title, session_id=request.session.session_key)
            newTask.save()

        return redirect('index')   

    else:

        tasks = Tasks.objects.filter(session_id = request.session.session_key)

        context = {
            "tasks":tasks,
        }

        return render(request, "Tasks/index.html", context=context)

def delete_task(request, pk):

    try:
        task = Tasks.objects.get(id=pk, session_id = request.session.session_key)
    except Tasks.DoesNotExist:
        pass
    
    task.delete()

    return redirect('index')



def edit_task(request,pk):

    task = Tasks.objects.get(id=pk, session_id = request.session.session_key)

    if request.method == "POST":

        #get new title from form
        new_title = request.POST.get("title")
        
        if new_title:
            task.title = new_title
            task.save()

        return redirect('index')
    
    else:

        return render(request, "Tasks/edit.html",{'task':task})