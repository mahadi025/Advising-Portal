# Generated by Django 3.2.9 on 2021-11-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]
