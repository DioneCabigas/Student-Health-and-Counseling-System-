from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Appointment, UserProfile
from .forms import AppointmentSchedulingForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.http import HttpResponse
from datetime import date
import calendar

def landing_page(request):
    return render(request, 'landing_page.html')

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
    appointments = Appointment.objects.filter(approval=True, is_done=False).order_by('-dateRequested', '-timeRequested')
    appointment_requests = Appointment.objects.filter(approval=False)   
    schedules = Appointment.objects.filter(approval=True, is_done=False).order_by('date', 'time')

    context = {
        'patients' : patients, 
        'appointments': appointments, 
        'appointment_requests': appointment_requests,
        'schedules' : schedules
    }
    return render(request, 'staff/dashboard.html', context)

@login_required
def schedule_view(request):
    appointments = Appointment.objects.filter(approval=True, is_done=False).order_by('date', 'time')

    context = {'appointments' : appointments}
    return render(request, 'staff/schedule.html', context)

# def schedule_view(request):
#     today = date.today()

#     # Get year, month, and day from query parameters
#     year = int(request.GET.get('year', today.year))
#     month_name = request.GET.get('month', calendar.month_abbr[today.month])
#     day = int(request.GET.get('day', today.day))

#     # Convert month name back to month number
#     try:
#         month = list(calendar.month_abbr).index(month_name)
#     except ValueError:
#         month = today.month  # Default to current month if invalid

#     start_date = date(year, month, 1)
#     end_date = date(year, month, calendar.monthrange(year, month)[1])
#     # Filter appointments from the specified day onward
#     appointments = Appointment.objects.filter(date__range=(start_date, end_date)).order_by('date')

#     # Pass abbreviated month names and days to the template
#     months = calendar.month_abbr[1:]  # Skip the empty first entry
#     days = list(range(1, calendar.monthrange(year, month)[1] + 1))  # Get days for the month

#     return render(request, 'staff/schedule.html', {'appointments': appointments, 'year': year, 'month': month_name, 'day': day, 'months': months, 'days': days,})

@login_required
def patient_view(request):
    patients = Patient.objects.all()
    appointment_requests = Appointment.objects.all()

    context = {'patients' : patients, 'appointment_requests' : appointment_requests}
    return render(request, 'staff/patient.html', context)

@login_required
def appointment_view(request):
    status = request.GET.get('status', 'not_done')  # Default to 'not_done'
    
    if status == 'done':
        appointments = Appointment.objects.filter(is_done=True).order_by('-dateRequested', '-timeRequested')
    else:  # 'not_done' or any other value defaults to this
        appointments = Appointment.objects.filter(approval=True, is_done=False).order_by('-dateRequested', '-timeRequested')

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
        appointment.delete()
        messages.success(request, "Appointment request deleted successfully!")
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
    return render(request, 'student/dashboard.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.get(user=request.user)
            Patient.objects.get_or_create(user=user_profile)
                
            form.instance.patient = user_profile
            form.save()
            
            return redirect('book_appointment')
    else:
        form = AppointmentSchedulingForm()

    context = {'form': form}
    return render(request, 'student/book_appointment.html', context)

def health_record(request):
    user_profile = request.user

    try:
        profile = user_profile.userprofile
    except UserProfile.DoesNotExist:
        profile = None

    return render(request, 'student/health_record.html', {'profile' : profile})

def edit_user_profile(request):
    # Retrieve the UserProfile instance
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Retrieve form data from POST request
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        middle_name = request.POST.get('middle_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # Update the fields if data is provided
        if student_id:
            user_profile.studentID = student_id
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

        # Save the updated UserProfile instance
        user_profile.save()

        # Redirect to the same page or another view (e.g., profile detail or list)
        return redirect('health_record')  # Replace with your URL name

    # Render the edit page if the request is GET
    return render(request, 'student/health_record.html', {'user_profile': user_profile})

def notification_view(request):
    return render(request, 'student/notification.html')

def prescription_view(request):
    return render(request, 'student/prescription.html')


# CHECK TO SEE IF AUTHENTICATED
def some_view(request):
    if request.user.is_authenticated:
        return HttpResponse("Hello, authenticated user!")
    else:
        return HttpResponse("You need to log in to access this page.")