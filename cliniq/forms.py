from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import *

class PatientForm (ModelForm):
    class Meta:
       model = Patient
       fields = '__all__'

class RDV_form(ModelForm):
    class Meta:
        model = RDV
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'temp': forms.TimeInput(attrs={'type': 'time'},format='%H:%M')
        }