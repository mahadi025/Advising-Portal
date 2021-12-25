# Generated by Django 3.2.9 on 2021-12-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisingslip',
            old_name='student',
            new_name='advisingStudent',
        ),
        migrations.AddField(
            model_name='advisingstudent',
            name='creditsTaken',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
    ]
