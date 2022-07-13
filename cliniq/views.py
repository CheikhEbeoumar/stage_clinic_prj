from hashlib import new
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect


def ajouter_patient(request):
    if request.method =='POST':
       form= PatientForm(request.POST)
       if form.is_valid():
        form.save()
        return  redirect('/patients')
        
    else:
        form=PatientForm()
    return render(request, 'cliniq/ajouter_patient.html',{'form':form})


def login(request):

    return render(request, 'cliniq/login.html')


def patients(request):
    patients = Patient.objects.all()
    context = {'patients':patients}
    return render(request, 'cliniq/patient.html', context)

def rdv(request,pk):
    patient = Patient.objects.get(id=pk)
    rdv = patient.rdv_set.all()
    
    context = {'rdv':rdv,'patient':patient}
    return render(request,'cliniq/RDV.html',context)
