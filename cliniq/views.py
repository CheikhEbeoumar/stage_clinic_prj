from hashlib import new
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def ajouter_patient(request):
    form_p = PatientForm()
    form_r = RDV_form()

    if request.method =='POST':
       form_p= PatientForm(request.POST)
       form_r= RDV_form(request.POST)
       if form_r.is_valid():
          form_p.save()
          form_r.save()
          redirect('patient')
       else:
          form_p =PatientForm()
          form_r =RDV_form()
          
    context = {'patient':form_p, 'rdv':form_r}
    return render(request, 'cliniq/ajouter_patient.html', context)


def login(request):

    return render(request, 'cliniq/login.html')


def patients(request):
    patient = Patient.objects.all()
    rdv = RDV.objects.all()
    patients = zip(patient,rdv)
    context = {'patients':patients}
    return render(request, 'cliniq/patient.html', context)
