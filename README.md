# Vibrant Mind 🧠 - Student Health and Counceling System 💊

Vibrant Mind is designed to support the physical and mental well-being of students in an educational environment. This system offers a wide range of health and counseling services, including medical care, psychological support, and resources for managing stress, anxiety, and other mental health concerns. It aims to create a safe and supportive atmosphere where students can access professional care, receive guidance, and thrive both academically and personally. Through this system, students are encouraged to take an active role in their health, helping them overcome challenges and achieve success in their academic journey.

## **Table of Contents**
1. [Documentation Purpose](#documentation-purpose)
2. [Documentation Scope](#documentation-scope)
3. [Functional Requirements](#functional-requirements)
   - [Login/Logout](#1-loginlogout)
   - [Appointment Scheduling](#2-appointment-scheduling)
   - [Health Record Management](#3-health-record-management)
   - [Counselor Assignment](#4-counselor-assignment)
   - [Health Alerts and Reminders](#5-health-alerts-and-reminders)
   - [Feedback and Satisfaction Surveys](#6-feedback-and-satisfaction-surveys)
4. [Code Overview](#code-overview)
   - [Landing Page](#landing-page)
   - [Account Management](#account-management)
   - [Staff Features](#staff-features)
   - [Student Features](#student-features)
   - [Utility Functions](#utility-functions)
5. [Supplementary Resources](#supplementary-resources)
   
---
## **Documentation Scope**

The scope includes:
- Offering a range of healthcare services like primary medical care and mental health counseling.
- Maintaining secure and confidential records of student interactions.
- Ensuring compliance with relevant health regulations and standards.

---

## **Documentation Purpose**

The purpose of this documentation is to outline the functionalities and scope of the **Student Health and Counseling System**, ensuring its proper usage, maintenance, and future enhancement.

---

## **Functional Requirements**

### **1. Login/Logout**
**Description**: Enables authorized users to securely log in and out of the system as administrators, counselors, or students.

---

### **2. Appointment Scheduling**
**Description**: Enables users to schedule appointments with relevant staff or administrators. The system confirms the details and notifies both parties.  
**Required Information**:
- Appointment Date
- Appointment Time
- Purpose of Appointment
- User's Full Name
- User's Email Address
- User's Contact Number
- Department or Staff Member
- Additional Notes or Special Requests

---

### **3. Health Record Management**
**Description**: Securely stores and manages students' health records, including medical history and visit notes.

---

### **4. Counselor Assignment**
**Description**: Administrators can assign counselors to students based on criteria such as availability and specialization. The system notifies both parties about the assignment.  
**Required Information**:
- Counselor's Full Name
- Counselor's Specialization
- Counselor's Availability
- Student's Full Name
- Student's ID Number
- Student's Contact Information
- Reason for Counseling
- Preferred Counselor (if any)
- Assignment Date
- Assignment Status (Active or Inactive)

---

### **5. Health Alerts and Reminders**
**Description**: Sends reminders for appointments, medication refills, and upcoming wellness events.

---

### **6. Feedback and Satisfaction Surveys**
**Description**: Gathers feedback through surveys to measure satisfaction with services and identify areas for improvement.

---

## Installation/Quick Start
After downloading the zip and opening it on your IDE, open terminal and follow these steps to get started:
> [!NOTE]
> You can also clone the repository and follow the steps

Create your virutal environment
```
py -m venv .venv
```
> You can replace `.venv` with any name for your virtual environment

Activate your virtual environment
```
.venv\Scripts\activate
```
Install the latest version of Django
```
pip install django
```
Change directory to VibrantMind
```
cd VibrantMind
```
Run `manage.py`
```
py manage.py runserver
```
## **Code Overview**

### **Landing Page**
- **Function**: `landing_page`
- **Description**: Renders the main landing page.
- **Template**: `landing_page.html`

---

### **Account Management**
- **Register View**: Handles user registration via `UserCreationForm`.
  - **Function**: `register_view`
  - **Template**: `account/signup.html`

- **Login View**: Authenticates and logs in users, redirecting them based on their roles.
  - **Function**: `login_view`
  - **Template**: `account/login.html`

- **Logout View**: Logs out users and redirects to the login page.
  - **Function**: `logout_view`

---

### **Staff Features**
1. **Dashboard**: Displays patient records, appointments, and schedules.
   - **Function**: `staff_dashboard_view`
   - **Template**: `staff/dashboard.html`

2. **Schedules**: Manages appointment schedules.
   - **Function**: `schedule_view`
   - **Template**: `staff/schedule.html`

3. **Patient Management**: Provides an interface for viewing and managing patient records.
   - **Function**: `patient_view`
   - **Template**: `staff/patient.html`

4. **Appointment Management**: Handles creating, updating, approving, and deleting appointments.
   - **Functions**:
     - `appointment_view`, `appointment_scheduling_view`
     - `appointment_request_view`, `update_appointment`
     - `mark_appointment_done`, `delete_appointment`
   - **Templates**:
     - `staff/appointment.html`
     - `staff/appointment_add_patient.html`
     - `staff/appointment_request.html`

---

### **Student Features**
1. **Dashboard**: Displays upcoming and completed consultations.
   - **Function**: `student_dashboard_view`
   - **Template**: `student/dashboard.html`

2. **Appointment Booking**: Allows students to book consultations.
   - **Function**: `book_appointment`
   - **Template**: `student/book_appointment.html`

3. **Health Records**: Displays students' health profiles.
   - **Function**: `health_record`
   - **Template**: `student/health_record.html`

4. **Profile Editing**: Enables students to update personal details.
   - **Function**: `edit_user_profile`
   - **Template**: `student/health_record.html`

5. **Notifications**: Displays notifications to students.
   - **Function**: `notification_view`
   - **Template**: `student/notification.html`

6. **Prescriptions**: Shows prescription details.
   - **Function**: `prescription_view`
   - **Template**: `student/prescription.html`

---

### **Utility Functions**
- **Authentication Check**: 
  - **Function**: `some_view`
  - **Description**: Displays a message based on user authentication.

---


## **Supplementary Resources**
- [Gantt Chart](https://docs.google.com/spreadsheets/d/18ITegzR5nr96ui4txSycWD-stPE5RqoX/edit?usp=sharing&ouid=117047969151162919748&rtpof=true&sd=true)
- [Entity-Relationship Diagram (ERD)](https://lucid.app/lucidchart/4c74fb05-7fa0-48a1-a0f1-983c81edd9e9/edit?viewport_loc=-928%2C-525%2C3006%2C1393%2C0_0&invitationId=inv_808b98d7-743d-4fd5-a221-b876e825ee2d)
- [UI/UX Design (Figma)](https://www.figma.com/design/V8Ndu64BYRfERFfN0XL3y5/%5BCSIT327%5D-Student-Health-and-Counseling-System?node-id=0-1&t=hXA9WwyIdoAZGIeb-1)

> Add the screenshot here
![Vibrant Mind ERD](https://github.com/DioneCabigas/Student-Health-and-Counseling-System-/blob/master/Student%20Health%20and%20Counseling%20System.png "VibrantMind ERD")

### Contributors
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/DioneCabigas" target="_blank" style="text-decoration: none;">
        <img src="https://avatars.githubusercontent.com/u/143990611?v=4" width="100px" height="100px" style="border-radius: 50%;" alt="Dione"/>
        <br />
        <b style="text-decoration: none;">Dione Alfred Cabigas</b>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Nicbites" target="_blank" style="text-decoration: none;">
        <img src="https://avatars.githubusercontent.com/u/120681026?v=4" width="100px" height="100px" style="border-radius: 50%;" alt="Nico"/>
        <br />
        <b style="text-decoration: none;">Nico Rivera</b>
      </a>
    </td>
  </tr>
</table>
