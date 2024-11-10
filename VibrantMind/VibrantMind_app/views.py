from django.shortcuts import render, redirect
from .models import Patient, Appointment, AppointmentRequest
from .forms import AppointmentSchedulingForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# @login_required
def dashboard_view(request):
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()
    appointment_requests = AppointmentRequest.objects.all()

    context = {'patients' : patients, 'appointments': appointments, 'appointment_requests': appointment_requests}
    return render(request, 'dashboard.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form" : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {"form" : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout')

def patient_view(request):
    patients = Patient.objects.all()

    context = {'patients' : patients}
    return render(request, 'patient.html', context)

def appointment_view(request):
    appointments = Appointment.objects.all()

    context = {'appointments': appointments}
    return render(request, 'appointment.html', context)

def appointment_scheduling_view(request):
    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentSchedulingForm()

    context = {'form': form}
    return render(request, 'appointment_add_patient.html', context)

def appointment_request_view(request):
    appointmentRequests = AppointmentRequest.objects.all()

    context = {'appointmentRequests': appointmentRequests}
    return render(request, 'appointment_request.html', context)

# STUDENT
def student_dashboard(request):
    return render(request, 'student/dashboard.html')

def book_appointment(request):
    if request.method == 'POST':
        pass
    return render(request, 'student/book_appointment.html')

def health_record(request):
    return render(request, 'student/health_record.html')