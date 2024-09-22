from django.db import models

# CABIGAS - APPOINTMENT SCHEDULING
class AppointmentSchedulingModel(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    # contactNum = models.CharField(max_length=11)
    staff = models.CharField(max_length=100)
    notes = models.TextField()