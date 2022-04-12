from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# function to render the home page
def frontend(request):
    return render(request, 'app/frontend.html')

# function to render the backend
@login_required(login_url="login")
def backend(request):
    return render(request, 'app/backend.html')

# function to add patient
@login_required(login_url="login")
def add_patient(request):
    return render(request, 'app/add.html')