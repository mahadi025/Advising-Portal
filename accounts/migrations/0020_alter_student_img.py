# Generated by Django 3.2.9 on 2021-11-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20211130_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.ImageField(blank=True, default='/images/DefaultProfilePic.jpg', null=True, upload_to='pics'),
        ),
    ]