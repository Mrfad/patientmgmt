from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Patient

# function to render the home page
def frontend(request):
    return render(request, 'app/frontend.html')

# function to render the backend
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patients_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone=q) | Q(email=q) | Q(gender=q) | Q(note__icontains=q)
        ).order_by('-created_at')
    else:
        all_patients_list = Patient.objects.all().order_by('-created_at')
    
    paginator = Paginator(all_patients_list, 5)
    page = request.GET.get('page')
    all_patients = paginator.get_page(page)
    context = {"patients":all_patients}
    return render(request, 'app/backend.html', context)
        

# function to add patient
@login_required(login_url="login")
def add_patient(request):
    if request.method == 'POST':
        if request.POST.get('name') \
                and request.POST.get('phone') \
                and request.POST.get('email') \
                and request.POST.get('age') \
                and request.POST.get('gender') \
                or request.POST.get('note'):
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

# function to delete patient
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, 'Patient deleted successfully')
    return HttpResponseRedirect('/backend')

# function to access the patient individually
@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient != None:
        return render(request, 'app/edit.html', {'patient':patient})


# function to edit the patient
@login_required(login_url="login")
def edit_patient(request):
    if request.method == 'POST':s
        patient = Patient.objects.get(id=request.POST.get('id'))
        if patient != None:
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save() 
            messages.success(request, 'Patient updated successfully')
            return HttpResponseRedirect('/backend')
