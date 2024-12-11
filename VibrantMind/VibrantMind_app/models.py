from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# USERS
class UserProfile(models.Model):
    USER_TYPE = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lastName = models.CharField(max_length=100, blank=True, null=True)
    firstName = models.CharField(max_length=100, blank=True, null=True)
    middleName = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.lastName} {self.firstName} - {self.user_type}'

# PATIENT
class Patient(models.Model):
    userProfile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.userProfile.user.username} - {self.userProfile.lastName}'
    
# NOT USED
class Staff(models.Model):
    PROFESSION = (
        ('Health Consultant', 'Health Consultant'),
        ('Councelor', 'Councelor')
    )
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50, choices=PROFESSION, null=True)

# APPOINTMENT | APPOINTMENT REQUEST
class Appointment(models.Model):
    SESSION_TYPE = (
        ('Health Service', 'Health Service'),
        ('Counceling Service', 'Counceling Service'),
    )
    STAFF_CHOICE = (
        ('Health Staff', 'Health Staff'),
        ('Counceling Staff', 'Counceling Staff'),
    )
    APPOINTMENT_TYPE = (
        ('Face-to-face', 'Face-to-Face'),
        ('Online', 'Online'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    session_type = models.CharField(max_length=100, choices=SESSION_TYPE, null=True)
    appointment_type = models.CharField(max_length=100, choices=APPOINTMENT_TYPE, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    staff = models.CharField(max_length=100, choices=STAFF_CHOICE, blank=True)
    notes = models.TextField(null=True)
    dateRequested = models.DateField(auto_now_add=True, null=True)
    timeRequested = models.TimeField(auto_now_add=True, null=True)
    approval = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)

    def __str__(self):
        return f'Appointment for {self.patient.userProfile.lastName} - {self.session_type} - {self.appointment_type} | Done: {self.is_done}'

# HEALTH RECORD
class HealthRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, null=True)
    medical_history = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Medical Record of {self.user}'
    
# PRESCRIPTION
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    medicine_name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.userProfile.user.username} - {self.medicine_name}"
