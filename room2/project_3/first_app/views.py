from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author':'Rahim Hossin','age': 1,'birthday':datetime.datetime.now(),'lst':['I','Love','Python'],'courses':[
        {
            'id': 1,
            'name': 'Python',
            'fees': 5000
        },
        {
            'id': 2,
            'name': 'Django',
            'fees': 4000
        },
        {
            'id': 3,
            'name': 'SDLC',
            'fees': 50000
        },
    ]}
    return render(request,'first_app/home.html',d)
