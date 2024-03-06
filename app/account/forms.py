from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Instructor, Student


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class EditStudentProfile(ModelForm):
    class Meta:
        model = Student
        fields = ["img", "phone_number", "present_address", "blood_group", "dept_name"]


class EditInstructorProfile(ModelForm):
    class Meta:
        model = Instructor
        fields = ["img", "phone_number", "present_address", "blood_group", "dept_name"]
