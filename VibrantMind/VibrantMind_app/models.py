from django.db import models

# USERS
class User(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.lastName}'

# PATIENT
class Patient(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    studentID = models.CharField(max_length=11)
    # lastName = models.CharField(max_length=100, null=True)
    # firstName = models.CharField(max_length=100, null=True)
    # middleName = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    # email = models.EmailField(null=True)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.studentID}|{self.user.lastName}'

# APPOINTMENT | APPOINTMENT REQUEST
class Appointment(models.Model):
    APPOINTMENT_TYPE = (
        ('Health Services', 'Health Services'),
        ('Counceling Services', 'Counceling Services'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=100)
    date = models.DateTimeField()
    staff = models.CharField(max_length=100)
    notes = models.TextField()
    # dateRequested = models.DateTimeField(auto_now_add=True, null=True)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.patient.user.lastName}, {self.patient.user.firstName}'

# APPOINTMENT REQUEST
# class AppointmentRequest(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     appointment_type = models.CharField(max_length=100)
#     date = models.DateTimeField()
#     staff = models.CharField(max_length=100)
#     notes = models.TextField()
#     dateRequested = models.DateTimeField(auto_now_add=True, null=True)
#     approval = models.BooleanField(default=False)

#     def __str__(self):
#         return f'{self.patient.user.lastName} - {self.appointment_type}'

