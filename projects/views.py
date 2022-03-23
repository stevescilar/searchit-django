from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def projects(request):
    return HttpResponse('here is where products dwell')

def  project(request,pk):
    return HttpResponse('Project Detail page')