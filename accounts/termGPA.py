from .models import *

def calculate(username,semester,year):
    takes=takes=Takes.objects.filter(takes_id=username,section__semester=semester,section__year=year)
    Grade = {
        "A+": 4.00,
        "A": 4.00,
        "A-": 3.70,
        "B+": 3.30,
        "B": 3.00,
        "B-": 2.70,
        "C+": 2.30,
        "C": 2.00,
        "C-": 1.70,
        "D+": 1.30,
        "D": 1.00,
        "F": 0.00
    }
    gp=0.0
    totalCredits=0.0
    for take in takes:
        if take.grade :
            gp+=float(Grade.get((take.grade)))*float((take.section.course.credits))
            totalCredits+=float((take.section.course.credits))
    if totalCredits!=0:
        result=gp/totalCredits
        result = "{:.2f}".format(result)
    else:
        result=0.0
    return result
