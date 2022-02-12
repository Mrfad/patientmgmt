from django.http import HttpResponse
from django.shortcuts import render

def frontend(request):
    return render(request, 'app/frontend.html')

def backend(request):
    return render(request, 'app/backend.html')
