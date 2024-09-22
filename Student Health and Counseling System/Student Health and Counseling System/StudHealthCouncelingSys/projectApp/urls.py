from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view),
    path('index.html', views.dashboard_view),
    path('appointment.html', views.appointment_view),
    path('appointmentAddPatient.html', views.appointment_scheduling_view)
]