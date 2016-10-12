from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sport(models.Model):
    sport=models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.sport)
class Calculate(models.Model):
    worker=models.ForeignKey(User)
    activ=models.BooleanField(default=False)
    sports=models.ForeignKey(Sport, blank=True)
    date=models.DateTimeField(auto_now=True,auto_now_add=True)
    def __unicode__(self):
        return unicode(self.worker)

    def creat(self, user):
        self.worker=user