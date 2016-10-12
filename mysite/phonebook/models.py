from django.db import models
import json




class Partner(models.Model):
    part_name=models.CharField(max_length=300)
    base_id=models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.part_name)


class Club(models.Model):
    club_name=models.CharField(max_length=100)
    partner=models.ForeignKey(Partner)
    base_id=models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.club_name)



class Cash(models.Model):
    cash_name=models.CharField(max_length=20)
    club=models.ForeignKey(Club)
    partner=models.ForeignKey(Partner)
    base_id=models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return unicode(self.cash_name)


class Roll(models.Model):
    roll_name=models.CharField(max_length=50)
    def __unicode__(self):
        return unicode(self.roll_name)

class Phone(models.Model):
    phone_number=models.IntegerField()
    coment=models.CharField(max_length=1000)
    partner=models.ForeignKey(Partner)
    club=models.ForeignKey(Club)
    cash=models.ForeignKey(Cash)
    rol=models.ForeignKey(Roll)
    def __unicode__(self):
        return unicode(self.phone_number)
# Create your models here.
