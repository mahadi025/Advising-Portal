from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from core.models import (
    Department,
    Classroom,
    Course,
    Instructor,
    Student,
    Section,
    TimeSlot,
    PrereqCourse,
    Advisor,
)


class Command(BaseCommand):
    help = "Seed data for the application"

    def handle(self, *args, **options):
        student_group, _ = Group.objects.get_or_create(name="student")
        instructor_group, _ = Group.objects.get_or_create(name="instructor")

        self.stdout.write(self.style.SUCCESS("Groups initialized successfully"))

        if not User.objects.filter(is_superuser=True).exists():
            admin_user = User.objects.create_superuser(
                username="admin", email="admin@example.com", password="admin"
            )
            admin_user.groups.add(student_group, instructor_group)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))

        if not Department.objects.exists():
            Department.objects.create(dept_name="CSE", building="Main Building")
            Department.objects.create(dept_name="EEE", building="AB1")
            Department.objects.create(dept_name="MPS", building="AB2")
            Department.objects.create(dept_name="ENG", building="Main Building")
            self.stdout.write(self.style.SUCCESS("Department initialized successfully"))

        if not Classroom.objects.exists():
            Classroom.objects.create(building="Main Building", room_number="201")
            Classroom.objects.create(building="Main Building", room_number="202")
            Classroom.objects.create(building="Main Building", room_number="203")
            Classroom.objects.create(building="Main Building", room_number="204")
            Classroom.objects.create(building="Main Building", room_number="205")
            Classroom.objects.create(building="Main Building", room_number="206")
            Classroom.objects.create(building="Main Building", room_number="301")
            Classroom.objects.create(building="Main Building", room_number="302")
            Classroom.objects.create(building="Main Building", room_number="303")
            Classroom.objects.create(building="Main Building", room_number="304")
            Classroom.objects.create(building="Main Building", room_number="305")
            Classroom.objects.create(building="Main Building", room_number="306")
            Classroom.objects.create(building="Main Building", room_number="401")
            Classroom.objects.create(building="Main Building", room_number="402")
            Classroom.objects.create(building="Main Building", room_number="403")
            Classroom.objects.create(building="Main Building", room_number="404")
            Classroom.objects.create(building="Main Building", room_number="405")
            Classroom.objects.create(building="Main Building", room_number="406")
            Classroom.objects.create(building="Main Building", room_number="501")
            Classroom.objects.create(building="Main Building", room_number="502")
            Classroom.objects.create(building="Main Building", room_number="503")
            Classroom.objects.create(building="Main Building", room_number="504")
            Classroom.objects.create(building="Main Building", room_number="505")
            Classroom.objects.create(building="Main Building", room_number="506")
            self.stdout.write(self.style.SUCCESS("Classroom initialized successfully"))

        if not Course.objects.filter(course_id="CSE103").exists():
            Course.objects.create(
                course_id="CSE103",
                title="Structure Programming",
                dept_name=Department.objects.get(dept_name="CSE"),
                credits=4.5,
            )
            self.stdout.write(self.style.SUCCESS("CSE103 created successfully"))
        if not Course.objects.filter(course_id="CSE106").exists():
            Course.objects.create(
                course_id="CSE106",
                title="Discrete Mathematics",
                dept_name=Department.objects.get(dept_name="CSE"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("CSE106 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="CSE106"),
                prereq=Course.objects.get(course_id="CSE103"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for CSE106"))
        if not Course.objects.filter(course_id="CSE110").exists():
            Course.objects.create(
                course_id="CSE110",
                title="Object Oriented Programming",
                dept_name=Department.objects.get(dept_name="CSE"),
                credits=4.5,
            )
            self.stdout.write(self.style.SUCCESS("CSE110 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="CSE110"),
                prereq=Course.objects.get(course_id="CSE106"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for CSE110"))
        if not Course.objects.filter(course_id="CSE200").exists():
            Course.objects.create(
                course_id="CSE200",
                title="Computer-Aided Engineering Drawing",
                dept_name=Department.objects.get(dept_name="CSE"),
                credits=1.0,
            )
            self.stdout.write(self.style.SUCCESS("CSE200 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="CSE200"),
                prereq=Course.objects.get(course_id="CSE110"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for CSE200"))
        if not Course.objects.filter(course_id="MAT101").exists():
            Course.objects.create(
                course_id="MAT101",
                title="Differential and Integral Calculus",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("MAT101 created successfully"))
        if not Course.objects.filter(course_id="MAT102").exists():
            Course.objects.create(
                course_id="MAT102",
                title="Differential Equations and Special Functions",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("MAT102 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="MAT102"),
                prereq=Course.objects.get(course_id="MAT101"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for MAT102"))
        if not Course.objects.filter(course_id="MAT104").exists():
            Course.objects.create(
                course_id="MAT104",
                title="Coordinate Geometry and Vector Analysis",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("MAT104 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="MAT104"),
                prereq=Course.objects.get(course_id="MAT102"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for MAT104"))
        if not Course.objects.filter(course_id="MAT205").exists():
            Course.objects.create(
                course_id="MAT205",
                title="Linear Algebra and Complex Variable",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("MAT205 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="MAT205"),
                prereq=Course.objects.get(course_id="MAT102"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for MAT205"))
        if not Course.objects.filter(course_id="ENG101").exists():
            Course.objects.create(
                course_id="ENG101",
                title="Basic English",
                dept_name=Department.objects.get(dept_name="ENG"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("ENG101 created successfully"))
        if not Course.objects.filter(course_id="ENG102").exists():
            Course.objects.create(
                course_id="ENG102",
                title="Composition and Communication Skills",
                dept_name=Department.objects.get(dept_name="ENG"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("ENG102 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="ENG102"),
                prereq=Course.objects.get(course_id="ENG101"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for ENG102"))
        if not Course.objects.filter(course_id="CHE109").exists():
            Course.objects.create(
                course_id="CHE109",
                title="Engineering Chemistry",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=4.0,
            )
            self.stdout.write(self.style.SUCCESS("CHE109 created successfully"))
        if not Course.objects.filter(course_id="PHY109").exists():
            Course.objects.create(
                course_id="PHY109",
                title="Engineering Physics-I (Introductory Classical Physics)",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=4.0,
            )
            self.stdout.write(self.style.SUCCESS("PHY109 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="PHY109"),
                prereq=Course.objects.get(course_id="MAT102"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for PHY109"))
        if not Course.objects.filter(course_id="PHY209").exists():
            Course.objects.create(
                course_id="PHY209",
                title="Engineering Physics-II (Introductory Quantum Physics)",
                dept_name=Department.objects.get(dept_name="MPS"),
                credits=3.0,
            )
            self.stdout.write(self.style.SUCCESS("PHY209 created successfully"))
            PrereqCourse.objects.create(
                course=Course.objects.get(course_id="PHY209"),
                prereq=Course.objects.get(course_id="PHY109"),
            )
            self.stdout.write(self.style.SUCCESS("Prereq Course added for PHY209"))

        if not Instructor.objects.filter(instructor_id="icse1"):
            instructor_user = User.objects.create_user(
                username="icse1",
                password="PleaseUnlock",
                first_name="CSE Instructor",
                last_name="One",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )

        if not Instructor.objects.filter(instructor_id="icse2"):
            instructor_user = User.objects.create_user(
                username="icse2",
                password="PleaseUnlock",
                first_name="CSE Instructor",
                last_name="Two",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )

        if not Instructor.objects.filter(instructor_id="icse3"):
            instructor_user = User.objects.create_user(
                username="icse3",
                password="PleaseUnlock",
                first_name="CSE Instructor",
                last_name="Three",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="icse4"):
            instructor_user = User.objects.create_user(
                username="icse4",
                password="PleaseUnlock",
                first_name="CSE Instructor",
                last_name="Four",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="icse5"):
            instructor_user = User.objects.create_user(
                username="icse5",
                password="PleaseUnlock",
                first_name="CSE Instructor",
                last_name="Five",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )

        if not Instructor.objects.filter(instructor_id="imps1"):
            instructor_user = User.objects.create_user(
                username="imps1",
                password="PleaseUnlock",
                first_name="MPS Instructor",
                last_name="One",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="MPS"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="imps2"):
            instructor_user = User.objects.create_user(
                username="imps2",
                password="PleaseUnlock",
                first_name="MPS Instructor",
                last_name="Two",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="MPS"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="imps3"):
            instructor_user = User.objects.create_user(
                username="imps3",
                password="PleaseUnlock",
                first_name="MPS Instructor",
                last_name="Three",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="MPS"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="imps4"):
            instructor_user = User.objects.create_user(
                username="imps4",
                password="PleaseUnlock",
                first_name="MPS Instructor",
                last_name="Four",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="MPS"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )

        if not Instructor.objects.filter(instructor_id="ieng1"):
            instructor_user = User.objects.create_user(
                username="ieng1",
                password="PleaseUnlock",
                first_name="ENG Instructor",
                last_name="One",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="ENG"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="ieng2"):
            instructor_user = User.objects.create_user(
                username="ieng2",
                password="PleaseUnlock",
                first_name="ENG Instructor",
                last_name="Two",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="ENG"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )
        if not Instructor.objects.filter(instructor_id="ieng3"):
            instructor_user = User.objects.create_user(
                username="ieng3",
                password="PleaseUnlock",
                first_name="ENG Instructor",
                last_name="Three",
            )
            instructor_user.groups.add(instructor_group)
            Instructor.objects.create(
                user=instructor_user,
                instructor_id=instructor_user.username,
                first_name=instructor_user.first_name,
                last_name=instructor_user.last_name,
                dept_name=Department.objects.get(dept_name="ENG"),
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Instructor {instructor_user.username} created successfully"
                )
            )

        if not Student.objects.exists():
            student_user = User.objects.create_user(
                username="2019-1-60-001",
                password="PleaseUnlock",
                first_name="Student",
                last_name="One",
            )
            student_user.groups.add(student_group)
            Student.objects.create(
                user=student_user,
                student_id=student_user.username,
                first_name=student_user.first_name,
                last_name=student_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            student_user = User.objects.create_user(
                username="2019-1-60-002",
                password="PleaseUnlock",
                first_name="Student",
                last_name="Two",
            )
            student_user.groups.add(student_group)
            Student.objects.create(
                user=student_user,
                student_id=student_user.username,
                first_name=student_user.first_name,
                last_name=student_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            student_user.groups.add(student_group)
            student_user = User.objects.create_user(
                username="2019-1-60-003",
                password="PleaseUnlock",
                first_name="Student",
                last_name="Three",
            )
            student_user.groups.add(student_group)
            Student.objects.create(
                user=student_user,
                student_id=student_user.username,
                first_name=student_user.first_name,
                last_name=student_user.last_name,
                dept_name=Department.objects.get(dept_name="CSE"),
            )
            self.stdout.write(self.style.SUCCESS("Students created successfully"))

        advisor, created = Advisor.objects.get_or_create(
            instructor=Instructor.objects.get(instructor_id="icse1"),
            student=Student.objects.get(student_id="2019-1-60-001"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "Instructor icse1 was assigned to 2019-1-60-001 as an advisor"
                )
            )

        advisor, created = Advisor.objects.get_or_create(
            instructor=Instructor.objects.get(instructor_id="icse1"),
            student=Student.objects.get(student_id="2019-1-60-002"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "Instructor icse1 was assigned to 2019-1-60-002 as an advisor"
                )
            )

        if not TimeSlot.objects.exists():
            TimeSlot.objects.create(
                time_slot_id="ST-1",
                day="ST",
                start_hr="8",
                start_min="30",
                end_hr="10",
                end_min="00",
            )
            TimeSlot.objects.create(
                time_slot_id="ST-2",
                day="ST",
                start_hr="10",
                start_min="10",
                end_hr="11",
                end_min="40",
            )
            TimeSlot.objects.create(
                time_slot_id="ST-3",
                day="ST",
                start_hr="11",
                start_min="50",
                end_hr="1",
                end_min="20",
            )
            TimeSlot.objects.create(
                time_slot_id="MW-1",
                day="MW",
                start_hr="8",
                start_min="30",
                end_hr="10",
                end_min="00",
            )
            TimeSlot.objects.create(
                time_slot_id="MW-2",
                day="MW",
                start_hr="10",
                start_min="10",
                end_hr="11",
                end_min="40",
            )
            TimeSlot.objects.create(
                time_slot_id="MW-3",
                day="MW",
                start_hr="11",
                start_min="50",
                end_hr="1",
                end_min="20",
            )
            TimeSlot.objects.create(
                time_slot_id="TR-1",
                day="TR",
                start_hr="8",
                start_min="30",
                end_hr="10",
                end_min="00",
            )
            TimeSlot.objects.create(
                time_slot_id="TR-2",
                day="TR",
                start_hr="10",
                start_min="10",
                end_hr="11",
                end_min="40",
            )
            TimeSlot.objects.create(
                time_slot_id="TR-3",
                day="TR",
                start_hr="11",
                start_min="50",
                end_hr="1",
                end_min="20",
            )
            TimeSlot.objects.create(
                time_slot_id="SR-1",
                day="SR",
                start_hr="8",
                start_min="30",
                end_hr="10",
                end_min="00",
            )
            TimeSlot.objects.create(
                time_slot_id="SR-2",
                day="SR",
                start_hr="10",
                start_min="10",
                end_hr="11",
                end_min="40",
            )
            TimeSlot.objects.create(
                time_slot_id="SR-3",
                day="SR",
                start_hr="11",
                start_min="50",
                end_hr="1",
                end_min="20",
            )
            self.stdout.write(self.style.SUCCESS("Time slots created successfully"))

        """CSE"""
        """Summer"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Spring"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Fall"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE103"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="201"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE106"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="202"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="CSE110"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="203"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="icse3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """MPS"""
        """Summer"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="4",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="4",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="306"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Fall"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="4",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="4",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="306"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Spring"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="301"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT101"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="302"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT102"),
            sec_id="4",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="303"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps4"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="SR-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT104"),
            sec_id="4",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="304"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="305"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="MAT205"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="306"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="TR-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="imps3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """ENG"""
        """Summer"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="4",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="1",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="2",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="3",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="4",
            semester="Summer",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Fall"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="4",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="1",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="2",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="3",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="4",
            semester="Fall",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))

        """Spring"""

        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG101"),
            sec_id="4",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="ST-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="1",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="2",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="401"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-2"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng3"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="3",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-1"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng1"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
        section, created = Section.objects.get_or_create(
            course=Course.objects.get(course_id="ENG102"),
            sec_id="4",
            semester="Spring",
            year=2021,
            classroom=Classroom.objects.get(
                building="Main Building", room_number="402"
            ),
            time_slot=TimeSlot.objects.get(time_slot_id="MW-3"),
            capacity=35,
            instructor=Instructor.objects.get(instructor_id="ieng2"),
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"{section.course.course_id} {section.sec_id} {section.semester} {section.year} created successfully with instructor {section.instructor.instructor_id}"
                )
            )
        else:
            self.stdout.write(self.style.ERROR("Unable to create section"))
