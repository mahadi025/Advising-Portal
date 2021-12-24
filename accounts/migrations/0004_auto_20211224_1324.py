# Generated by Django 3.2.9 on 2021-12-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211224_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.CharField(choices=[('Spring', 'Spring'), ('Fall', 'Fall'), ('Summer', 'Summer')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(blank=True, choices=[('C-', 'C-'), ('C', 'C'), ('D', 'D'), ('F', 'F'), ('A-', 'A-'), ('B+', 'B+'), ('D+', 'D+'), ('B', 'B'), ('B-', 'B-'), ('A+', 'A+'), ('A', 'A'), ('C+', 'C+')], max_length=2, null=True),
        ),
    ]
