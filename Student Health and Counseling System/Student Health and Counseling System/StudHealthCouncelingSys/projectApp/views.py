from django.shortcuts import render
from .forms import AppointmentSchedulingForm

# CABIGAS - APPOINTMENT SCHEDULING
def dashboard_view(request):
    return render(request, 'index.html')

def appointment_view(request):
    return render(request, 'appointment.html')

def appointment_scheduling_view(request):
    form = AppointmentSchedulingForm()

    if request.method == 'POST':
        form = AppointmentSchedulingForm(request.POST)
        if form.is_valid():
            form.save()
            form = AppointmentSchedulingForm()

    context = {'form': form}
    return render(request, 'appointmentAddPatient.html', context)