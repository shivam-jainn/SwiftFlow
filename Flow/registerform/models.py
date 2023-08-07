from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

COLLEGE_CHOICES = (
    ('Reva University','Reva University'),
    ('SPIJM','SPIJM')
)

ROLE_CHOICES = (
    ('Ride Taker', 'RIDE TAKER'),
    ('Ride Giver', 'RIDE GIVER')
)

class SwiftUser(AbstractUser):
    username = models.CharField(max_length=40,unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    collegeID = models.ImageField(upload_to='collegeid_pics/')
    profile_pic = models.ImageField(upload_to='profile_pics/')
    license_pic = models.ImageField(upload_to='license_pics/')
    collegeName = models.CharField(max_length=100, choices=COLLEGE_CHOICES)
    location = models.JSONField()

class Ride(models.Model):
    rideid = models.IntegerField()
    price = models.PositiveSmallIntegerField()