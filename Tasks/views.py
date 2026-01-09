from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    if request.method == "POST":
        task = request.POST.get("task")

        print(task)

        
       

        return redirect('index')   #  IMPORTANT

  
    return render(request, "Tasks/index.html")