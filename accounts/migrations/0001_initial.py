# Generated by Django 3.2.9 on 2021-11-23 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('budget', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('instructor_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('dept_name', models.ForeignKey(blank=True, db_column='i_dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec_id', models.CharField(max_length=8)),
                ('semester', models.CharField(choices=[('Spring', 'Spring'), ('Fall', 'Fall'), ('Summer', 'Summer')], max_length=6)),
                ('year', models.DecimalField(decimal_places=0, max_digits=4)),
                ('time_slot_id', models.CharField(blank=True, max_length=4, null=True)),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.classroom')),
                ('course', models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.course')),
            ],
            options={
                'unique_together': {('course', 'sec_id', 'semester', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('tot_cred', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True)),
                ('dept_name', models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot_id', models.CharField(max_length=10)),
                ('day', models.CharField(max_length=2)),
                ('start_hr', models.DecimalField(decimal_places=0, max_digits=2)),
                ('start_min', models.DecimalField(decimal_places=0, max_digits=2)),
                ('end_hr', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('end_min', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
            ],
            options={
                'unique_together': {('time_slot_id', 'day', 'start_hr', 'start_min')},
            },
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.section')),
                ('teaches_id', models.ForeignKey(db_column='instructor_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.section')),
                ('takes_id', models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(blank=True, db_column='dept_name', null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.department'),
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
