from django.db import models

# Create your models here.


class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=30)
    password = models.CharField("password",max_length=20)

class user(models.Model):
    userid=models.AutoField(primary_key=True)
    firstname = models.CharField("firstname",max_length=30)
    lastname = models.CharField("lastname",max_length=30)
    email = models.EmailField("email",max_length=30)
    phone = models.CharField("phone",max_length=20)
    address = models.TextField("address")