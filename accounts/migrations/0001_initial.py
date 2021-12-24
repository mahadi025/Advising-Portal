# Generated by Django 3.2.9 on 2021-12-23 20:24

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=15)),
                ('room_number', models.CharField(max_length=7)),
                ('capacity', models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True)),
            ],
            options={
                'unique_together': {('building', 'room_number')},
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('credits', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('building', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructorId', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.ImageField(default='DefaultProfilePic.jpg', null=True, upload_to='pics')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('bloodGroup', models.CharField(blank=True, choices=[('B+', 'B+'), ('A+', 'A+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('A-', 'A-'), ('O+', 'O+')], max_length=3, null=True)),
                ('presentAddress', models.CharField(blank=True, max_length=60, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=14, null=True)),
                ('dept_name', models.ForeignKey(blank=True, db_column='i_dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.ImageField(default='DefaultProfilePic.jpg', null=True, upload_to='pics')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('tot_cred', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('bloodGroup', models.CharField(blank=True, choices=[('B+', 'B+'), ('A+', 'A+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('A-', 'A-'), ('O+', 'O+')], max_length=3, null=True)),
                ('presentAddress', models.CharField(blank=True, max_length=60, null=True)),
                ('phoneNumber', models.CharField(blank=True, max_length=14, null=True)),
                ('completedCourses', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=8), blank=True, size=10)),
                ('dept_name', models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot_id', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=2)),
                ('start_hr', models.CharField(max_length=2)),
                ('start_min', models.CharField(max_length=2)),
                ('end_hr', models.CharField(max_length=2)),
                ('end_min', models.CharField(max_length=2)),
            ],
            options={
                'unique_together': {('time_slot_id', 'day', 'start_hr', 'start_min')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secId', models.CharField(max_length=8)),
                ('semester', models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=6)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.classroom')),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.instructor')),
                ('timeSlot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.timeslot')),
            ],
            options={
                'unique_together': {('course', 'secId', 'semester', 'year', 'timeSlot'), ('semester', 'year', 'timeSlot', 'instructor'), ('secId', 'course', 'semester', 'year'), ('semester', 'year', 'timeSlot', 'course'), ('classroom', 'semester', 'year', 'timeSlot')},
            },
        ),
        migrations.AddField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department'),
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, choices=[('D+', 'D+'), ('C-', 'C-'), ('A-', 'A-'), ('A', 'A'), ('C', 'C'), ('B', 'B'), ('A+', 'A+'), ('F', 'F'), ('C+', 'C+'), ('B+', 'B+'), ('D', 'D'), ('B-', 'B-')], max_length=2, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.section')),
                ('takes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('takes_id', 'section')},
            },
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CourseId', to='accounts.course')),
                ('prereq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PreReqId', to='accounts.course')),
            ],
            options={
                'unique_together': {('course', 'prereq')},
            },
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('s', models.OneToOneField(db_column='s_ID', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.student')),
                ('i', models.ForeignKey(blank=True, db_column='i_ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.instructor')),
            ],
        ),
    ]
