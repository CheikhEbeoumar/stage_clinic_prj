from msilib.schema import ListView
from django.urls import reverse
from hashlib import new
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseForbidden
from django.views.generic import(CreateView,ListView,TemplateView,DetailView,FormView,UpdateView,DeleteView) 
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy


class PatientListView(ListView):
    model= Patient
    template_name ='cliniq/patient.html'
    context_object_name='patient'

class PatientCreateView(CreateView):
    model=Patient
    form_class=PatientForm
    template_name= 'cliniq/ajouter_patient.html'
    def form_valid(self, form):

        return super().form_valid(form)

class PatientDetailView(DetailView):
    model= Patient
    template_name ='cliniq/RDV.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PatientUpdateView(UpdateView):
    model = Patient
    form_class= PatientForm
    pk_url_kwarg = 'pk'
    template_name = 'cliniq/update_patient.html'
    success_url = reverse_lazy('patients')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients')
   

class RDVCreateView(CreateView):
    model=RDV
    form_class= RDV_form
    template_name= 'cliniq/ajouter_rdv.html'
    



   


# def ajouter_patient(request,):
#     if request.method =='POST':
#        form= PatientForm(request.POST)
#        if form.is_valid():
#         form.save()
#         return  redirect('/patients')
        
#     else:
#         form=PatientForm()
#     return render(request, 'cliniq/ajouter_patient.html',{'form':form})

# def ajouter_rdv(request,pk):
#     form= RDV_form()
#     if request.method =='POST':
#        form = RDV_form(request.POST)
       
#        if form.is_valid():
#         form.save()
#         return  redirect('RDV')
        
#     else:
#         form = RDV_form()
#     return render(request,'cliniq/ajouter_rdv.html',{'form':form})

# def patients(request):
#     patients = Patient.objects.all()
#     context = {'patients':patients}
#     return render(request, 'cliniq/patient.html', context)

# def rdv(request,pk):
#     patient = Patient.objects.get(id=pk)
#     rdv = patient.rdv_set.all()
    
#     context = {'rdv':rdv,'patient':patient}
#     return render(request,'cliniq/RDV.html',context)
