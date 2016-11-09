from django.db import models
from django.contrib.auth.models import User
class Logger_Action(models.Model):
    user = models.ForeignKey(User)
    action_name = models.CharField(max_length=40)
    action=models.CharField(max_length=100, blank=True )
    time=models.DateTimeField(auto_now=False, auto_now_add=True)
    object_name=models.CharField(max_length=40)
    object=models.CharField(max_length=40)
    user_ip=models.CharField(max_length=15, blank=True)
# Create your models here.
