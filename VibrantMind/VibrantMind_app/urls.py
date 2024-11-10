from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.dashboard_view, name='dashboard'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('signup.html', views.register_view, name='register'),
    path('login.html', views.login_view, name='login'),
    path('logout.html', views.logout_view, name='logout'),
    path('patient.html', views.patient_view, name='patient_list'),
    path('appointment.html', views.appointment_view, name='appointment_list'),
    path('appointment_add_patient.html', views.appointment_scheduling_view),
    path('appointment_request.html', views.appointment_request_view, name='appointment_request'),
    # STUDENT
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/book-appointment/', views.book_appointment, name='book_appointment'),
    path('student/health-record/', views.health_record, name='health_record'),
]