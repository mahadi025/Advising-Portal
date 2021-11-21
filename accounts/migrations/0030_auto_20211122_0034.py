# Generated by Django 3.2.9 on 2021-11-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20211122_0033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('B+', 'B+'), ('B+', 'B-'), ('A-', 'A-'), ('A+', 'A+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('ICE', 'ICE'), ('CSE', 'CSE'), ('BBA', 'BBA'), ('EEE', 'EEE'), ('ENG', 'ENG')], max_length=5, null=True),
        ),
    ]