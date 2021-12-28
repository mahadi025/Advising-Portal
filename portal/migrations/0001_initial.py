# Generated by Django 3.2.9 on 2021-12-27 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvisingStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditsTaken', models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='AdvisingSlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisingStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.advisingstudent')),
                ('section', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.section')),
            ],
        ),
    ]
