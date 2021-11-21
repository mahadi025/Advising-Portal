# Generated by Django 3.2.9 on 2021-11-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20211121_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=0, max_length=255, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B-'), ('O+', 'O+'), ('AB+', 'AB+'), ('B+', 'B+'), ('A-', 'A-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('ENG', 'ENG'), ('CSE', 'CSE'), ('BBA', 'BBA'), ('ICE', 'ICE'), ('EEE', 'EEE')], max_length=5, null=True),
        ),
    ]