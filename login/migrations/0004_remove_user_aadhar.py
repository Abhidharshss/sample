# Generated by Django 3.2.16 on 2023-01-04 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user_aadhar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='aadhar',
        ),
    ]
