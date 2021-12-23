# Generated by Django 3.2.9 on 2021-12-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211223_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instructor',
            name='completedCourses',
        ),
        migrations.AddField(
            model_name='student',
            name='completedCourses',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('A-', 'A-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(blank=True, choices=[('C+', 'C+'), ('F', 'F'), ('B+', 'B+'), ('A-', 'A-'), ('D', 'D'), ('C-', 'C-'), ('A+', 'A+'), ('C', 'C'), ('B-', 'B-'), ('A', 'A'), ('D+', 'D+'), ('B', 'B')], max_length=2, null=True),
        ),
    ]
