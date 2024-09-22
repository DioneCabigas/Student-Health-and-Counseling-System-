from django import forms
from django.forms import ModelForm, widgets
from . import models

#CABIGAS
class AppointmentSchedulingForm(ModelForm):
    class Meta:
        model = models.AppointmentSchedulingModel
        fields = '__all__'
        widgets = {
            'lastName' : forms.TextInput(attrs={'class' : 'form-control'}),
            'firstName' : forms.TextInput(attrs={'class' : 'form-control'}),
        }