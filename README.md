# Advising Portal

### Both student and instructor can create an account with their student id or instructor id. An email will also be created with that student id or instructor id.

#### P.S By default the email will be created like this student_id@ewubd.edu.

### They can edit their personal info and change their profile picture.

### Students can see their class schedule for each semester(Summer, Spring, Fall).

### Instructor can also see their class schedule and can be able to change the grade of the student who have taken that course.

### Student can go to the advising section to take courses for their next semester and print the advising slip.

### Advisor of a student can also add courses for them.

### Student can also see their cgpa for each semester(if a grade is given).

### Student and Instructor can reset their password.

## How to use

### 1. Clone or download the repository.

### 2. Go to that directory then open a terminal/command prompt and can create a virtual environment.

```
python -m venv env
or
python3 -m venv env
```

### 3. Activate the environment.

```
Windows
env\scripts\activate
Linux
source env/bin/activate
```

### 4. Install all the requirements.

```
pip install -r requirements.txt
```

### 5 Create a .env file. In that file copy the followings.

```
SECRET_KEY=give-secret-key-here
DEBUG=1

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'your password'
```

#### P.S Your normal email password wont work here. You need to go to https://myaccount.google.com/apppasswords to generate a password for your app. Create a new password for your app and then copy that password here.

### 6. Go to app directory

```
cd app
```

### 7. Migrate the database.

```
python manage.py migrate
```

### 6. Generate seed data. It is not necessary but in order for the app to work you need to create some groups for the user they are "student" and "instructor". You can create them by yourselves by going to the admin panel. The groups will automatically be created while seeding the data.

```
python manage.py seed
```

#### P.S It will create some students, instructor, sections, classrooms, departments etc. A superuser will also be created.

### 7. Run the app

```
python manage.py runserver
```

### 8. Go to http://127.0.0.1:8000 to see the website.

### 9. You can login using seed data or create your own account.

#### Seed data

```
Student
student_id=2019-1-60-001, password=PleaseUnlock
student_id=2019-1-60-002, password=PleaseUnlock
student_id=2019-1-60-003, password=PleaseUnlock

Instructor

instructor_id=icse1, password=PleaseUnlock
instructor_id=icse2, password=PleaseUnlock
instructor_id=icse3, password=PleaseUnlock
instructor_id=icse4, password=PleaseUnlock
instructor_id=icse5, password=PleaseUnlock
instructor_id=ieng1, password=PleaseUnlock
instructor_id=ieng2, password=PleaseUnlock
instructor_id=ieng3, password=PleaseUnlock
instructor_id=imps1, password=PleaseUnlock
instructor_id=imps2, password=PleaseUnlock
instructor_id=imps3, password=PleaseUnlock

Superuser
username=admin, password=admin
```
