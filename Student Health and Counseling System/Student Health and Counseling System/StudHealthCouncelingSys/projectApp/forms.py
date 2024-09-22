from django import forms
from django.forms import ModelForm, widgets
from . import models

# CABIGAS - APPOINTMENT SCHEDULING
class AppointmentSchedulingForm(ModelForm):
    class Meta:
        model = models.AppointmentSchedulingModel
        fields = '__all__'
        widgets = {
            'lastName' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder': ''}),
            'firstName' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder': ''}),
            'middleName' : forms.TextInput(attrs={'class': 'form-control', 'id' : 'floatingInput', 'placeholder': ''}),
            'staff' : forms.TextInput(attrs={'class' : 'form-select', 'placeholder': 'Select a Staff'}),
            'email' : forms.TextInput(attrs={'class' : 'form-control', 'id' : 'floatingInput', 'placeholder': ''}),
            'notes' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Additional Notes'}),
            'date' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'}),
            'time' : forms.TimeInput(attrs={'class' : 'form-control', 'type': 'time'}),
        }