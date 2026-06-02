from django.db import models

# Create your models here.

# model-->>serializer-->> view-->> template


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=13)

class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name

