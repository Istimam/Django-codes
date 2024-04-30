from django.shortcuts import render
from django.http import HttpResponse
# J:\PhitronBatch@3\Code\7. Software Development Project\Week 03 Introduction to DJANGO\room2\project_2\Templates\index.html
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is a home page")
def contact(request):
    return HttpResponse("This is a contact page")