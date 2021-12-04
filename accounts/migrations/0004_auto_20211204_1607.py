# Generated by Django 3.2.9 on 2021-12-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211204_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A+', 'A+'), ('B+', 'B+'), ('A-', 'A-'), ('AB-', 'AB-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='semester',
            field=models.CharField(choices=[('Summer', 'Summer'), ('Fall', 'Fall'), ('Spring', 'Spring')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A+', 'A+'), ('B+', 'B+'), ('A-', 'A-'), ('AB-', 'AB-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(blank=True, choices=[('F', 'F'), ('D', 'D'), ('C-', 'C-'), ('B+', 'B+'), ('A-', 'A-'), ('C', 'C'), ('D+', 'D+'), ('A', 'A'), ('A+', 'A+'), ('B-', 'B-'), ('B', 'B'), ('C+', 'C+')], max_length=2, null=True),
        ),
    ]
