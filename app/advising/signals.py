from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from core.models import AdvisingSlip, Takes, Student


@receiver(post_save, sender=AdvisingSlip)
def create_advising_slip(sender, instance, created, **kwargs):
    if created:
        instance.semester = instance.section.semester
        instance.year = instance.section.year
        instance.course = instance.section.course.course_id
        instance.timeSlot = instance.section.time_slot
        advising_student = instance.advising_student
        section = instance.section
        takes = Takes.objects.create(
            takes_id=advising_student.student, section=section, grade="NONE"
        )
        section.capacity -= 1
        section.save()
        takes.save()
        instance.advising_student.save()
        instance.save()


@receiver(post_delete, sender=AdvisingSlip)
def delete_advising_slip(sender, instance, **kwargs):
    if Takes.objects.filter(
        section=instance.section, takes_id=instance.advising_student.student
    ):
        takes = Takes.objects.get(
            section=instance.section, takes_id=instance.advising_student.student
        )
        takes.delete()
    instance.advising_student.credits_taken -= instance.section.course.credits
    if instance.advising_student.credits_taken < 0:
        instance.advising_student.credits_taken = 0
    instance.section.capacity += 1
    instance.section.save()
    day1 = instance.section.time_slot.day[0]
    day2 = instance.section.time_slot.day[1]
    if day1 == "S" and day2 == "T":
        instance.advising_student.sunday_class -= 1
        instance.advising_student.tuesday_class -= 1
        if (
            instance.advising_student.sunday_class < 0
            and instance.advising_student.tuesday_class < 0
        ):
            instance.advising_student.sunday_class = 0
            instance.advising_student.tuesday_class = 0
    elif day1 == "M" and day2 == "W":
        instance.advising_student.monday_class -= 1
        instance.advising_student.wednesday_class -= 1
        if (
            instance.advising_student.monday_class < 0
            and instance.advising_student.wednesday_class < 0
        ):
            instance.advising_student.monday_class = 0
            instance.advising_student.wednesday_class = 0
    elif day1 == "T" and day2 == "R":
        instance.advising_student.tuesday_class -= 1
        instance.advising_student.thursday_class -= 1
        if (
            instance.advising_student.tuesday_class < 0
            and instance.advising_student.thursday_class < 0
        ):
            instance.advising_student.tuesday_class = 0
            instance.advising_student.thursday_class = 0
    elif day1 == "S" and day2 == "R":
        instance.advising_student.sunday_class -= 1
        instance.advising_student.thursday_class -= 1
        if (
            instance.advising_student.sunday_class < 0
            and instance.advising_student.thursday_class < 0
        ):
            instance.advising_student.sunday_class = 0
            instance.advising_student.thursday_class = 0
    instance.advising_student.save()


@receiver(post_delete, sender=Takes)
def delete_course(sender, instance, **kwargs):
    Takes.objects.filter(section=instance.section).delete()
