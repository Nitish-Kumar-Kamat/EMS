import email
from pyexpat import model
from django.db import models

class AdminDatabase(models.Model):
    Firstname=models.CharField(max_length=50,null=False)
    Lastname=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=50,null=False)
    Contact=models.IntegerField(null=False)
    Password=models.CharField(max_length=50,null=False)

