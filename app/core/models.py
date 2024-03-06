from django.db import models
from django.contrib.auth.models import User


BLOOD_GROUP_LIST = [
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("O+", "O+"),
    ("O-", "O-"),
]

SEM_LIST = {("Summer", "Summer"), ("Fall", "Fall"), ("Spring", "Spring")}


GRADE_LIST = {
    ("A+", "A+"),
    ("A", "A"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B", "B"),
    ("B-", "B-"),
    ("C+", "C+"),
    ("C", "C"),
    ("C-", "C-"),
    ("D+", "D+"),
    ("D", "D"),
    ("F", "F"),
    ("NONE", "NONE"),
}


class Department(models.Model):
    dept_name = models.CharField(max_length=30)
    building = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.dept_name


class Instructor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    img = models.ImageField(null=True, default="DefaultProfilePic.jpg")
    instructor_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    dept_name = models.ForeignKey(Department, models.CASCADE, blank=True, null=True)
    email = models.EmailField(null=True, blank=True, max_length=254)
    blood_group = models.CharField(
        max_length=3, null=True, blank=True, choices=BLOOD_GROUP_LIST
    )
    present_address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} {self.instructor_id} {self.dept_name}"
        )

    def save(self, *args, **kwargs):
        if not self.email:
            self.user.email = f"{self.instructor_id.lower()}@std.ewubd.edu"
            self.email = self.user.email
            self.user.save()
        super().save(*args, **kwargs)


class CompletedCourse(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    semester = models.CharField(max_length=20, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.student_id} completed {self.course.course_id}"


class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    img = models.ImageField(null=True, default="DefaultProfilePic.jpg")
    student_id = models.CharField(max_length=13, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    dept_name = models.ForeignKey(Department, models.CASCADE, blank=True, null=True)
    email = models.EmailField(null=True, blank=True, max_length=254)
    # total_credits = models.DecimalField(
    #     max_digits=3,
    #     decimal_places=1,
    #     blank=True,
    #     null=True,
    #     default=0.0,
    #     editable=True,
    # )
    blood_group = models.CharField(
        max_length=3, null=True, blank=True, choices=BLOOD_GROUP_LIST
    )
    present_address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=14, null=True, blank=True)
    completed_courses = models.ManyToManyField("Course", through="CompletedCourse")

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

    def save(self, *args, **kwargs):
        if not self.email:
            self.user.email = f"{self.student_id}@std.ewubd.edu"
            self.email = self.user.email
            self.user.save()
        super().save(*args, **kwargs)


class Advisor(models.Model):
    student = models.OneToOneField(Student, models.CASCADE, null=True, blank=True)
    instructor = models.ForeignKey(Instructor, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.instructor.instructor_id


class Course(models.Model):
    course_id = models.CharField(max_length=8, unique=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    dept_name = models.ForeignKey(Department, models.CASCADE, blank=True, null=True)
    credits = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    # credits_required = models.DecimalField(
    #     max_digits=4, decimal_places=1, blank=True, null=True, default=0.0
    # )

    def __str__(self):
        return f"{self.course_id} {self.dept_name}"


class PrereqCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course")
    prereq = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="prereq_course"
    )

    class Meta:
        unique_together = ("course", "prereq")

    def __str__(self):
        return str(self.course.course_id) + " <-- " + str(self.prereq.course_id)


class Classroom(models.Model):
    building = models.CharField(max_length=15)
    room_number = models.CharField(max_length=7)

    class Meta:
        unique_together = ("building", "room_number")

    def __str__(self):
        return f"{self.building}-{self.room_number}"


class TimeSlot(models.Model):
    time_slot_id = models.CharField(max_length=10)
    day = models.CharField(max_length=2)
    start_hr = models.CharField(max_length=2)
    start_min = models.CharField(max_length=2)
    end_hr = models.CharField(max_length=2)
    end_min = models.CharField(max_length=2)

    class Meta:
        unique_together = ("time_slot_id", "day", "start_hr", "start_min")

    def __str__(self):
        return self.time_slot_id


class Section(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    sec_id = models.CharField(max_length=8)
    semester = models.CharField(max_length=6, choices=SEM_LIST)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    classroom = models.ForeignKey(Classroom, models.CASCADE)
    time_slot = models.ForeignKey(TimeSlot, models.CASCADE)
    capacity = models.DecimalField(
        max_digits=2, null=True, blank=True, decimal_places=0
    )
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)

    class Meta:
        unique_together = (
            ("course", "sec_id", "semester", "year", "time_slot"),
            ("classroom", "semester", "year", "time_slot"),
            ("semester", "year", "time_slot", "instructor"),
            ("sec_id", "course", "semester", "year"),
        )

    def __str__(self):
        return f"{self.course.course_id} ({self.sec_id} {self.semester} {str(self.year)}) - {self.instructor.instructor_id}"


class Takes(models.Model):
    takes_id = models.ForeignKey(Student, models.CASCADE)
    grade = models.CharField(max_length=4, blank=True, null=True, choices=GRADE_LIST)
    section = models.ForeignKey(Section, models.CASCADE)

    class Meta:
        unique_together = ("takes_id", "section")

    def __str__(self):
        return f"{self.takes_id.student_id} ({self.section.course.course_id} {self.section.semester} {str(self.section.year)})"


class AdvisingStudent(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    credits_taken = models.DecimalField(
        max_digits=3, decimal_places=1, blank=True, null=True, default=0, editable=True
    )
    sunday_class = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True, default=0, editable=True
    )
    monday_class = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True, default=0, editable=True
    )
    tuesday_class = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True, default=0, editable=True
    )
    wednesday_class = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True, default=0, editable=True
    )
    thursday_class = models.DecimalField(
        max_digits=1, decimal_places=0, null=True, blank=True, default=0, editable=True
    )

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.student.student_id}"


class AdvisingSlip(models.Model):
    advising_student = models.ForeignKey(AdvisingStudent, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    course = models.CharField(max_length=8, null=True, blank=True)
    semester = models.CharField(max_length=6, null=True, blank=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    time_slot = models.ForeignKey(
        TimeSlot, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        unique_together = (
            "course",
            "semester",
            "year",
            "advising_student",
            "section",
            "time_slot",
        )

    def __str__(self):
        return f"{self.advising_student.student.student_id} {self.section.course.course_id} {self.section.semester} {self.section.year}"
