from django.contrib import admin
from .models import Patient, Appointment, UserProfile

admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Appointment)
# admin.site.register(AppointmentRequest)
