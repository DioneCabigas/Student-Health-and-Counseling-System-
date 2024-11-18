from django.contrib import admin
from .models import Patient, Appointment, User

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Appointment)
# admin.site.register(AppointmentRequest)
