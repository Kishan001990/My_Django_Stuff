from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def help(request):
    help_dict = {'help_insert':'HELP PAGE'}
    return render(request,'appTwo',context=help_dict)