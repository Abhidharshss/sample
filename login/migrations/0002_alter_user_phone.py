# Generated by Django 3.2.16 on 2022-12-29 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='phone'),
        ),
    ]
