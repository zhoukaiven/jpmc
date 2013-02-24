from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FundraisingGroup(models.Model):
    group_name = models.CharField(max_length=50)
    fundraiser_name = models.CharField(max_length=50)
    
    current = models.IntegerField(default=0)
    goal = models.IntegerField()
    num_donations = models.IntegerField(default=0)
    
class User(models.Model):
    authUser = models.OneToOneField(User)
    group = models.ForeignKey(FundraisingGroup)
    
