from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Patient

# function to render the home page
def frontend(request):
    return render(request, 'app/frontend.html')

# function to render the backend
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        

# function to add patient
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, 'Patient added successfully')
            return HttpResponseRedirect('/backend')
    else:
        return render(request, "app/add.html")
