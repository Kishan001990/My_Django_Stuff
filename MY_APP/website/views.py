from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def home(request):
    isActive = True
    if request.method == 'POST':
        check=request.POST.get('check')
        if check is None: isActive=False
        else: isActive=True


    date=datetime.datetime.now()
    name="Jofra Archer"
    list_of_programs=[
        'WAP to check even or odd',
        'WAP to check prime number',
        'WAP to print all prime numbers from 1 to 100',
        'WAP to print pascals triangle'
    ]
    student={
        'student_name':"Rahul",
        'student_college':"ZYZ",
        'student_city':'LUCKNOW'
    }

    data = {
        'date':date,
        'name':name,
        'isActive':isActive,
        'list_of_programs':list_of_programs,
        'student_data':student

    }

    return render(request,"home.html",data)


def about(request):
    print("About page loaded")
    return render(request,"about.html",{})


def services(request):
    print("Services page loaded")
    return render(request,"services.html",{})
