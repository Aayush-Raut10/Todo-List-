from django.shortcuts import render, redirect
from django.http import HttpResponse
from Tasks.models import Tasks

# Create your views here.
def index(request):
    
    if request.method == "POST":
        task = request.POST.get("title")

        print(task)

        newTask = Tasks(title=task)
        newTask.save()

        
        return redirect('index')   #  IMPORTANT

    else:

        tasks = Tasks.objects.all()

        context = {
            "tasks":tasks,
        }
    return render(request, "Tasks/index.html", context=context)