from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class Scheldue(models.Model):
    start_working=models.TimeField(auto_now=False, auto_now_add=False)
    start_break=models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    end_break = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    end_working = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        if self.start_break != None and self.end_break != None:
            return (f"{self.start_working} to {self.start_break} and {self.end_break} to {self.end_working}")
        else:
            return (f"{self.start_working} to {self.end_working}")

class WorkLocation(models.Model):
    name=models.CharField(max_length=100)
    adress=models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.adress} , {self.name}")

class User(AbstractUser):
    is_customer=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)


class Worker(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    location=models.ForeignKey(WorkLocation,on_delete=models.PROTECT)
    CATEGORY = ('Cardiologist','Cardiologist'),('Dentist', 'Dentist'),('Dermatologist', 'Dermatologist'),('Ophthalmologist', 'Ophthalmologist'),('Surgeon', 'Surgeon')
    Specialisation = models.CharField(max_length=50,choices=CATEGORY)
    scheldue=models.ForeignKey(Scheldue,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name}. Specialization: {self.Specialisation}")


class Client(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return (f"{self.user.first_name} {self.user.last_name}")

class Reservation(models.Model):
    PROCEDURE = [('Consultation', 'Consultation'), ('Operation', 'Operation')]

    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    docid=models.ForeignKey(Worker,on_delete=models.CASCADE)
    procedure = models.CharField(max_length=50, choices=PROCEDURE,default=PROCEDURE[1],null=True)
    day = models.DateField(auto_now=False, auto_now_add=False,null=True)
    start_reserv = models.TimeField(auto_now=False, auto_now_add=False,null=True)
    end_reserv = models.TimeField(auto_now=False, auto_now_add=False,null=True)

    def __str__(self):
        return (f"{self.client.user.first_name} {self.client.user.last_name} Date: {self.day} Time: from {self.start_reserv} to {self.end_reserv}")