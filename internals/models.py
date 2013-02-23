from django.db import models

# Create your models here.

class FundraisingGroup(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    authUser = models.OneToOneField(User)
    group = models.ForeignKey(Group)
