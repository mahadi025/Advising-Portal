from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from core.models import Takes, Student, AdvisingSlip, CompletedCourse


@receiver(post_save, sender=Takes)
def update_grade(sender, instance, **kwargs):
    student = Student.objects.get(student_id=instance.takes_id.student_id)
    year = instance.section.year
    semester = instance.section.semester
    if instance.grade == "F" or instance.grade == "NONE":
        if CompletedCourse.objects.filter(
            student=student, course=instance.section.course
        ).exists():
            student.completed_courses.remove(instance.section.course)
    else:
        if not CompletedCourse.objects.filter(
            student=student, course=instance.section.course
        ).exists():
            CompletedCourse.objects.create(
                student=student,
                course=instance.section.course,
                semester=semester,
                year=year,
            )
    student.save()
