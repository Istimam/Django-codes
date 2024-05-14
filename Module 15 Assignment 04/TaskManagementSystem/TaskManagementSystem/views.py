from django.shortcuts import render
from task.models import Task
# Create your views here.
def task_list(request):
    data = Task.objects.all()
    print(data)
    return render(request, 'home.html',{'data':data})