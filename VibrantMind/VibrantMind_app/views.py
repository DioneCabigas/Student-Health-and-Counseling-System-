from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Appointment, UserProfile, Prescription
from .forms import AppointmentSchedulingForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponse
from datetime import date
import calendar

# ACCOUNT
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {"form" : form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data = request.POST)
        
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('dashboard_redirect')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'account/login.html', {"form" : form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                user_profile = UserProfile.objects.get(user=user)
                print(user_profile)
                if user_profile.user_type == 'student':
                    return redirect('student_dashboard')
                elif user_profile.user_type == 'staff':
                    return redirect('staff_dashboard')
            except UserProfile.DoesNotExist:
                return HttpResponse("User profile not found.")
        else:
            return render(request, 'account/login.html', {'error': 'Invalid credentials'})

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# STAFF
@login_required
def staff_dashboard_view(request):
    patients = Patient.objects.all()    
    appointments = Appointment.objects.filter(approval=True, is_done=False, is_removed=False).order_by('-dateRequested', '-timeRequested')
    appointment_requests = Appointment.objects.filter(approval=False)   
    schedules = Appointment.objects.filter(approval=True, is_done=False, is_removed=False).order_by('date', 'time')

    context = {
        'patients' : patients, 
        'appointments': appointments, 
        'appointment_requests': appointment_requests,
        'schedules' : schedules
    }
    return render(request, 'staff/dashboard.html', context)

@login_required
def schedule_view(request):
    appointments = Appointment.objects.filter(approval=True, is_done=False, is_removed=False).order_by('date', 'time')

    context = {'appointments' : appointments}
    return render(request, 'staff/schedule.html', context)

@login_required
def patient_view(request):
    patients = Patient.objects.all()
    appointment_requests = Appointment.objects.all()

    context = {'patients' : patients, 'appointment_requests' : appointment_requests}
    return render(request, 'staff/patient.html', context)

@login_required
def appointment_view(request):
    status = request.GET.get('status', 'not_done')  # Default: Not Done
    
    if status == 'done':
        appointments = Appointment.objects.filter(is_done=True).order_by('-dateRequested', '-timeRequested')
    else:
        appointments = Appointment.objects.filter(approval=True, is_done=False, is_removed=False).order_by('-dateRequested', '-timeRequested')

    context = {'appointments': appointments}
    return render(request, 'staff/appointment.html', context)

@login_required
def appointment_scheduling_view(request):
    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentSchedulingForm()

    context = {'form': form}
    return render(request, 'staff/appointment_add_patient.html', context)

@login_required
def appointment_request_view(request):
    appointment_requests = Appointment.objects.filter(approval=False)

    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentSchedulingForm()

    context = {'appointment_requests': appointment_requests, 'form': form}
    return render(request, 'staff/appointment_request.html', context)

@login_required
def update_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)

        staff = request.POST.get('staff')
        appointment_type =request.POST.get('appointment_type')
        date = request.POST.get('date')
        time = request.POST.get('time')

        if staff:
            appointment.staff = staff
        if staff:
            appointment.appointment_type = appointment_type
        if date:
            appointment.date = date
        if time:
            appointment.time = time

        appointment.approval = True
        appointment.save()

        return redirect('appointment_request')

    return render(request, 'staff/appointment_request.html')

@login_required
def mark_appointment_done(request, appointment_id):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.is_done = True
        appointment.save()
        messages.success(request, "Appointment marked as completed!")
    return redirect('appointment_list')

@login_required
def delete_appointment(request, appointment_id):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.is_removed = True
        appointment.save()
        # appointment.delete()
        messages.success(request, "Appointment request deleted!")
        return redirect(reverse('appointment_list'))
    return redirect(reverse('appointment_list'))

@login_required
def delete_appointmentRequest(request, appointment_id):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.delete()
        messages.success(request, "Appointment request deleted successfully!")
        return redirect(reverse('appointment_request'))
    return redirect(reverse('appointment_request'))

# STUDENT
@login_required
def student_dashboard_view(request):
    # Get the user's profile
    user_profile = UserProfile.objects.get(user=request.user)

    # Fetch upcoming consultations
    upcoming_consultations = Appointment.objects.filter(
        # patient=user_profile, 
        approval=True, 
        is_done=False
    ).order_by('date', 'time')

    # Fetch completed consultations
    completed_consultations = Appointment.objects.filter(
        # patient=user_profile, 
        is_done=True
    ).order_by('-date', '-time')[:5]  # Limit to the last 5 consultations

    # Context for rendering
    context = {
        'upcoming_consultations': upcoming_consultations,
        'completed_consultations': completed_consultations,
    }
    return render(request, 'student/dashboard.html', context)

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            patient, created = Patient.objects.get_or_create(userProfile=user_profile)
                
            form.instance.patient = patient
            form.save()
            
            return redirect('book_appointment')
    else:
        form = AppointmentSchedulingForm()

    context = {'form': form}
    return render(request, 'student/book_appointment.html', context)

def health_record(request):
    user = request.user

    try:
        profile = user.userprofile
        patient = Patient.objects.get(userProfile=profile)
    except (UserProfile.DoesNotExist, Patient.DoesNotExist):
        profile = None
        patient = None

    return render(request, 'student/health_record.html', {'profile' : profile, 'patient' : patient, 'user' : user})

def edit_user_profile(request):

    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':

        user_id = request.POST.get('user_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')

        if user_id:
            user_profile.userID = user_id
        if first_name:
            user_profile.firstName = first_name
        if last_name:
            user_profile.lastName = last_name
        if middle_name:
            user_profile.middleName = middle_name
        if gender:
            user_profile.gender = gender
        if age:
            user_profile.age = age
        if email:
            user_profile.email = email

        user_profile.save()

        return redirect('health_record')

    return render(request, 'student/health_record.html', {'user_profile': user_profile})

def notification_view(request):
    return render(request, 'student/notification.html')

def prescription_view(request):
    user = request.user

    try:
        patient = user.userprofile.patient
    except AttributeError:
        patient = None

    print(patient)

    # Only filter prescriptions if patient exists
    prescriptions = Prescription.objects.filter(patient=patient) if patient else []

    return render(request, 'student/prescription.html', {
        'prescriptions': prescriptions,
    })


def add_prescription(request, patient_id):
    # Retrieve the patient instance
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        # Extract prescription details from the form
        medicine_name = request.POST.get('medicine_name')
        dosage = request.POST.get('dosage')
        duration = request.POST.get('duration')
        
        # Create a new prescription for the patient
        prescription = Prescription.objects.create(
            patient=patient,  # Associate with the patient
            medicine_name=medicine_name,
            dosage=dosage,
            duration=duration
        )
        
        # Optionally, you can redirect to a page or back to the appointment list
        return redirect('appointment_list')  # Redirect to appointments page or any relevant view

    return HttpResponse("Invalid request method", status=400)

# CHECK TO SEE IF AUTHENTICATED
def some_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello, authenticated user!")
    else:
        return HttpResponse("You need to log in to access this page.")