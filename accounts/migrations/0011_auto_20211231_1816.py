# Generated by Django 3.2.9 on 2021-12-31 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20211231_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('A+', 'A+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('A+', 'A+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(blank=True, choices=[('C+', 'C+'), ('B+', 'B+'), ('C', 'C'), ('C-', 'C-'), ('D', 'D'), ('A-', 'A-'), ('B', 'B'), ('A+', 'A+'), ('A', 'A'), ('F', 'F'), ('B-', 'B-'), ('D+', 'D+')], max_length=2, null=True),
        ),
    ]
