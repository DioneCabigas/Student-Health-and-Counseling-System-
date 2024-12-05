from django.urls import path, include
from . import views

urlpatterns = [
    # ACCOUNT
    path('signup.html', views.register_view, name='register'),      
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path("accounts/", include("django.contrib.auth.urls")),
    path('', views.staff_dashboard_view, name='staff_dashboard'),

    # STAFF
    # path('', views.dashboard_view, name='dashboard'),
    path('staff/dashboard/', views.staff_dashboard_view, name='staff_dashboard'),
    path('staff/patient/', views.patient_view, name='patient_list'),
    path('staff/appointment/', views.appointment_view, name='appointment_list'),
    path('staff/appointment_add_patient/', views.appointment_scheduling_view),
    path('staff/appointment_request/', views.appointment_request_view, name='appointment_request'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointmentRequest, name='delete_appointmentRequest'),
    path('appointments/done/<int:appointment_id>/', views.mark_appointment_done, name='mark_appointment_done'),
    path('staff/schedule/', views.schedule_view, name='schedule_list'),
    # Filter
    path('schedule/<int:year>/<int:month>/', views.schedule_view, name='schedule_filtered'),

    # STUDENT
    path('student/dashboard/', views.student_dashboard_view, name='student_dashboard'),
    path('student/book-appointment/', views.book_appointment, name='book_appointment'),
    path('student/health-record/', views.health_record, name='health_record'),
    path('edit-profile/', views.edit_user_profile, name='edit_user_profile'),
    path('student/notification/', views.notification_view, name='notification'),
    path('student/prescription/', views.prescription_view, name='prescription'),

    path('test', views.some_view, name='test'),
]