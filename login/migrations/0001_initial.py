# Generated by Django 3.2.16 on 2022-12-29 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('logid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('password', models.CharField(max_length=20, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30, verbose_name='firstname')),
                ('lastname', models.CharField(max_length=30, verbose_name='lastname')),
                ('email', models.EmailField(max_length=30, verbose_name='email')),
                ('phone', models.IntegerField(verbose_name='phone')),
                ('address', models.TextField(verbose_name='address')),
            ],
        ),
    ]
