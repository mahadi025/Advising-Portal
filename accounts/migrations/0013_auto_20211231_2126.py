# Generated by Django 3.2.9 on 2021-12-31 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20211231_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('AB-', 'AB-'), ('A+', 'A+'), ('B+', 'B+'), ('A-', 'A-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('AB-', 'AB-'), ('A+', 'A+'), ('B+', 'B+'), ('A-', 'A-'), ('AB+', 'AB+'), ('O-', 'O-'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='takes',
            name='grade',
            field=models.CharField(blank=True, choices=[('D', 'D'), ('B-', 'B-'), ('C', 'C'), ('A+', 'A+'), ('B+', 'B+'), ('F', 'F'), ('A-', 'A-'), ('C-', 'C-'), ('A', 'A'), ('C+', 'C+'), ('B', 'B'), ('D+', 'D+')], max_length=2, null=True),
        ),
    ]
