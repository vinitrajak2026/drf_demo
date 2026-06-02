from django.db import models
class UserModel(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=250)
    password=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
# Create your models here.
