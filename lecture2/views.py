from django.http import HttpResponse
from django.shortcuts import render

def fx(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def services(request):
    return HttpResponse("Radhe Radhe This is our services Page")
