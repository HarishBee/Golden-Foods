from django.db import models

# Create your models here.
class register(models.Model):
    Name=models.CharField(max_length=30 )
    Mobile=models.CharField(max_length=10 , blank=True,null=True)
    Email=models.EmailField(unique=True)
    Date_of_birth=models.DateField()
    gender_choice=[('M','Male'),('F','Female'),('O','Other')]
    Gender=models.CharField(max_length=1 , choices=gender_choice)

class password(models.Model):
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20 )
    
class forget(models.Model):
    New_password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20 )