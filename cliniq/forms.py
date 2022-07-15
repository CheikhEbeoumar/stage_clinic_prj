from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import *


class PatientForm (ModelForm):
    class Meta:
       model = Patient
       fields = '__all__'
       widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class RDV_form(ModelForm):
    class Meta:
        model = RDV
        fields = '__all__'

        patient = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple)
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'temp': forms.TimeInput(attrs={'type': 'time'},format='%H:%M')
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
    