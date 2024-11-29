from django import forms
from django.forms import ModelForm, widgets
from . import models

# CABIGAS - APPOINTMENT SCHEDULING
class AppointmentSchedulingForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['appointment_type', 'date', 'time', 'notes', 'staff']
        widgets = {
            'appointment_type': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder' : 'Additional Notes...'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.DateInput(attrs={'class': 'form-control', 'type': 'time'}),
            'staff': forms.Select(attrs={'class': 'form-control'}),
        }