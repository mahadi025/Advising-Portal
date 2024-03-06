from django.shortcuts import render, redirect
from core.models import (
    Section,
    AdvisingStudent,
    AdvisingSlip,
    Student,
    PrereqCourse,
    Advisor,
)
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

year = 2021
semester = "Summer"


def is_instructor(user):
    return user.groups.filter(name="instructor").exists()


def set_advising_student_id(student_id):
    global advising_student_id
    advising_student_id = student_id


@login_required(login_url="login")
def advising(request):
    offered_sections = Section.objects.filter(year=year, semester=semester).order_by(
        "id"
    )
    group = request.user.groups.all()[0].name
    if group == "student":
        student = request.user.student
        advising_student, created = AdvisingStudent.objects.get_or_create(
            student=student
        )
    else:
        student = Student.objects.get(student_id=advising_student_id)
        advising_student, created = AdvisingStudent.objects.get_or_create(
            student=student
        )
    advised_sections = AdvisingSlip.objects.filter(
        advising_student=advising_student,
        section__semester=semester,
        section__year=year,
    )
    context = {
        "offered_sections": offered_sections,
        "advised_sections": advised_sections,
        "year": year,
        "semester": semester,
    }
    return render(request, "advising/advising.html", context)


@login_required(login_url="login")
def add_course(request, pk):
    group = request.user.groups.all()[0].name
    if group == "student":
        advising_student, created = AdvisingStudent.objects.get_or_create(
            student=request.user.student
        )
    else:
        student = Student.objects.get(student_id=advising_student_id)
        advising_student, created = AdvisingStudent.objects.get_or_create(
            student=student
        )
    section = Section.objects.get(id=pk)
    semester = section.semester
    year = section.year
    course = section.course.course_id
    time_slot = section.time_slot
    advising_student.credits_taken += section.course.credits
    day1 = section.time_slot.day[0]
    day2 = section.time_slot.day[1]
    if day1 == "S" and day2 == "T":
        advising_student.sunday_class += 1
        advising_student.tuesday_class += 1
    elif day1 == "M" and day2 == "W":
        advising_student.monday_class += 1
        advising_student.wednesday_class += 1
    elif day1 == "T" and day2 == "R":
        advising_student.tuesday_class += 1
        advising_student.thursday_class += 1
    elif day1 == "S" and day2 == "R":
        advising_student.sunday_class += 1
        advising_student.thursday_class += 1
    student = Student.objects.get(student_id=advising_student.student.student_id)
    if section.capacity > 0:
        if PrereqCourse.objects.filter(course=section.course):
            prereq = PrereqCourse.objects.get(course=section.course)
            prereq_course = prereq.prereq
            if student.completed_courses.filter(course_id=prereq.prereq.course_id):
                if advising_student.credits_taken <= 13.5:
                    if (
                        advising_student.sunday_class <= 2
                        and advising_student.monday_class <= 2
                        and advising_student.tuesday_class <= 2
                        and advising_student.wednesday_class <= 2
                        and advising_student.thursday_class <= 2
                    ):
                        if not AdvisingSlip.objects.filter(
                            advising_student=advising_student, course=course
                        ):
                            if not AdvisingSlip.objects.filter(
                                advising_student=advising_student,
                                time_slot=time_slot,
                            ):
                                advising_slip, created = (
                                    AdvisingSlip.objects.get_or_create(
                                        advising_student=advising_student,
                                        section=section,
                                        semester=semester,
                                        year=year,
                                        course=course,
                                        time_slot=time_slot,
                                    )
                                )
                                if created:
                                    messages.success(
                                        request,
                                        f"Successfully added {advising_slip.section.course.course_id}",
                                    )
                            else:
                                messages.error(request, "Time slot conflicted")
                        else:
                            messages.error(request, f"{course} already taken")
                    else:
                        messages.error(
                            request, "You can not take more than 2 classes per day"
                        )
                else:
                    messages.error(request, "Maximum 13.5 credits can be taken")
            else:
                messages.error(request, f"{prereq_course.course_id} not completed")
        else:
            if advising_student.credits_taken <= 13.5:
                if (
                    advising_student.sunday_class <= 2
                    and advising_student.monday_class <= 2
                    and advising_student.tuesday_class <= 2
                    and advising_student.wednesday_class <= 2
                    and advising_student.thursday_class <= 2
                ):
                    if not AdvisingSlip.objects.filter(
                        advising_student=advising_student, course=course
                    ):
                        if not AdvisingSlip.objects.filter(
                            advising_student=advising_student, time_slot=time_slot
                        ):
                            advising_slip, created = AdvisingSlip.objects.get_or_create(
                                advising_student=advising_student,
                                section=section,
                                semester=semester,
                                year=year,
                                course=course,
                                time_slot=time_slot,
                            )
                            if created:
                                messages.success(
                                    request,
                                    f"Successfully added {advising_slip.section.course.course_id}",
                                )
                        else:
                            messages.error(request, "Time slot conflicted")
                    else:
                        messages.error(request, f"{course} already taken")
                else:
                    messages.error(
                        request, "You can not take more than 2 classes per day"
                    )
            else:
                messages.error(request, "Maximum 13.5 credits can be taken")
    else:
        messages.error(request, f"No seat available for {course} {section.sec_id}")

    return redirect("advising")


@login_required(login_url="login")
def delete_course(request, pk):
    advising_slip = AdvisingSlip.objects.get(id=pk)
    messages.success(
        request,
        f"Successfully deleted {advising_slip.section.course.course_id}",
    )
    advising_slip.delete()
    return redirect("advising")


@login_required(login_url="login")
def print_slip(request):
    group = request.user.groups.all()[0].name
    if group == "student":
        advising_student = AdvisingStudent.objects.get(student=request.user.student)
        advised_sections = AdvisingSlip.objects.filter(
            advising_student=advising_student,
            section__semester=semester,
            section__year=year,
        )
    else:
        student = Student.objects.get(student_id=advising_student_id)
        advising_student = AdvisingStudent.objects.get(student=student)
        advised_sections = AdvisingSlip.objects.filter(
            advising_student=advising_student,
            section__semester=semester,
            section__year=year,
        )
    context = {
        "student": student,
        "advised_sections": advised_sections,
        "advising_student": advising_student,
    }
    return render(request, "advising/slip.html", context)


@login_required(login_url="login")
@user_passes_test(is_instructor, login_url="login")
def advisor_advising(request):
    instructor = request.user.instructor
    offered_sections = Section.objects.filter(year=year, semester=semester).order_by(
        "id"
    )
    if request.method == "POST":
        student_id = request.POST["student_id"]
        if Student.objects.filter(student_id=student_id):
            student = Student.objects.get(student_id=student_id)
            set_advising_student_id(student_id)
            if Advisor.objects.filter(instructor=instructor, student=student):
                return redirect("advising")
            else:
                messages.error(request, "You are not his/her Advisor")
        else:
            messages.error(request, "No student found")
    return render(request, "advising/select_student.html")
