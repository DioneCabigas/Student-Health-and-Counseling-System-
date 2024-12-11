# Vibrant Mind 🧠 - Student Health and Counceling System 💊

Vibrant Mind is designed to support the physical and mental well-being of students in an educational environment. This system offers a wide range of health and counseling services, including medical care, psychological support, and resources for managing stress, anxiety, and other mental health concerns. It aims to create a safe and supportive atmosphere where students can access professional care, receive guidance, and thrive both academically and personally. Through this system, students are encouraged to take an active role in their health, helping them overcome challenges and achieve success in their academic journey.

## System Overview
### Core Components
1. **Login Module**  
   - Secure authentication using Django's built-in user model.
   - Role-based access for students and staff.

2. **Dashboard**  
   - A central hub tailored for different user roles:
   - Students: View appointments, prescriptions, notifications, and health records.
   - Counseling Staff: Access patient lists and scheduled appointments.
   
3. **Book Appointment Module**  
   - Students can book appointments with healthcare or counseling staff.
   - Options for service type, reason, and preferred date.

4. **Health Records Management**  
   - Comprehensive repository of medical and counseling histories for each student.
   - Easy access to records for both students and staff.

5. **Prescription Management**  
   - Add and view prescribed medications, dosage, and duration.

6. **Notification System**  
   - Keeps users informed about new appointments, reminders, and other important updates.

7. **Appointment Management**  
   - Staff can manage appointment schedules and approvals.
   - Status updates for students regarding their appointment requests.

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

## Documents
### Gantt Chart
To view our groups progress, click here to view our [Gantt Chart](https://docs.google.com/spreadsheets/d/1ZJAgBEXDusqZ-mhCv4EqpkDiCW66DiFIDaX5OVUyMtY/edit?usp=sharing).

### ERD
Vibrant Mind's Entity Relationship Diagram
![Vibrant Mind ERD](https://github.com/DioneCabigas/Student-Health-and-Counseling-System-/blob/master/Student%20Health%20and%20Counseling%20System.png "VibrantMind ERD")

### UI/UX FIGMA
> Add the screenshot here

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
