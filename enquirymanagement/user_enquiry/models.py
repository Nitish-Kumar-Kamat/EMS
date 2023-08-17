from django.db import models

class UserDatabase(models.Model):
    Firstname=models.CharField(max_length=50,null=False)
    Lastname=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=50,null=False)
    Contact=models.IntegerField(null=False)
    Password=models.CharField(max_length=50,null=False)


class EnquiryDatabase(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(max_length=50,null=False)
    Contact=models.IntegerField(null=False)
    Address=models.CharField(max_length=100,null=False)
    Query=models.CharField(max_length=200,null=False)

