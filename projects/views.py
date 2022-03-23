from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def projects(request):
    context = {}
    return render (request,'projects/projects.html',context)

def  project(request,pk):
    context = {}
    return render (request,'projects/single-project.html',context)