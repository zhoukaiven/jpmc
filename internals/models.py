from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=50)
    ext_color = models.CharField(max_length=1, choices = [('w','white'),('g','green'),('y','yellow'),('r','red')])
    int_color = models.CharField(max_length=1, choices = [('b','blue'),('g','green'),('y','yellow')])
    outhouse_color = models.CharField(max_length=1, choices = [('b','blue'),('w','white')])

class FundraisingGroup(models.Model):
    group_name = models.CharField(max_length=50)
    fundraiser_name = models.CharField(max_length=50)
    school = models.ForeignKey(School)
    
    #fcid
    description = models.TextField()
    
    current = models.IntegerField(default=0)
    goal = models.IntegerField()
    num_donations = models.IntegerField(default=0)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    group = models.ForeignKey(FundraisingGroup, null=True)

    
