# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Found_duplicates(models.Model):
    event1_id=models.CharField(max_length=15)
    event2_id = models.CharField(max_length=15)
    event1_date=models.DateTimeField(auto_now_add=False)
    event2_date=models.DateTimeField(auto_now_add=False)
    event1_name=models.CharField(max_length=100, blank=True, default="")
    event2_name = models.CharField(max_length=100, blank=True, default="")
    event1_team1=models.CharField(max_length=100, blank=True)
    event1_team2 = models.CharField(max_length=100, blank=True)
    event2_team1 = models.CharField(max_length=100, blank=True)
    event2_team2 = models.CharField(max_length=100, blank=True)
    event1_sport = models.CharField(max_length=100)
    event2_sport = models.CharField(max_length=100)
    event1_provider = models.CharField(max_length=15, blank=True, null=True)
    event2_provider = models.CharField(max_length=15, blank=True, null=True)
    logging_id=models.IntegerField(blank=True, null=True)
    #exception=models.BooleanField(default=False)

    def save(self,*args, **kwargs):
        loging_event=Logging_duplicates()
        loging_event.event1_id=self.event1_id
        loging_event.event2_id = self.event2_id
        loging_event.event1_date = self.event1_date
        loging_event.event2_date = self.event2_date
        loging_event.event1_team1 = self.event1_team1
        loging_event.event1_team2 = self.event1_team2
        loging_event.event2_team1 = self.event2_team1
        loging_event.event2_team2 = self.event2_team2
        loging_event.event1_sport = self.event1_sport
        loging_event.event2_sport = self.event2_sport
        loging_event.event1_provider = self.event1_provider
        loging_event.event2_provider = self.event2_provider
        loging_event.save()
        log_id=loging_event.id
        #print(log_id)
        self.logging_id=log_id
        super(Found_duplicates,self).save(*args, **kwargs)
    def delete(self, using=None, *args, **kwargs):
        #print self.logging_id
        log_event=Logging_duplicates.objects.get(id=self.logging_id)
        date=datetime.utcnow()
        log_event.date_ended_duble=date
        log_event.save()
        super(Found_duplicates, self).delete(*args, **kwargs)

    def __unicode__(self):
        return unicode(self.event1_id)+u" - "+unicode(self.event2_id)


class Exceptions(models.Model):
    Symptom=models.CharField(max_length=100)
    text=models.CharField(max_length=100)
    coment=models.CharField(max_length=1000, blank=True, default="")
    user=models.ForeignKey(User, null=True)


class Logging_duplicates(models.Model):
    event1_id = models.CharField(max_length=15)
    event2_id = models.CharField(max_length=15)
    event1_date = models.DateTimeField(auto_now_add=False)
    event2_date = models.DateTimeField(auto_now_add=False)
    event1_name = models.CharField(max_length=100, blank=True, default="")
    event2_name = models.CharField(max_length=100, blank=True, default="")
    event1_team1 = models.CharField(max_length=100, blank=True)
    event1_team2 = models.CharField(max_length=100, blank=True)
    event2_team1 = models.CharField(max_length=100, blank=True)
    event2_team2 = models.CharField(max_length=100, blank=True)
    event1_sport = models.CharField(max_length=100)
    event2_sport = models.CharField(max_length=100)
    event1_provider=models.CharField(max_length=15, blank=True, null=True)
    event2_provider = models.CharField(max_length=15, blank=True, null=True)
    exception = models.BooleanField(default=False)
    date_started_duble=models.DateTimeField(auto_now_add=True)
    date_ended_duble=models.DateTimeField(auto_now_add=False, null=True)
    def __unicode__(self):
        return unicode(self.event1_name+"  "+unicode(self.date_started_duble)+" - "+unicode(self.date_ended_duble))
class Parser_duble_event(models.Model):
    site_name=models.CharField(max_length=100)
    pars_url=models.URLField(max_length=200,)
    login=models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    proxy_addr=models.CharField(max_length=100, blank=True)
    proxy_port = models.CharField(max_length=5, blank=True)
    def __unicode__(self):
        return unicode(self.site_name)
class Audio_file(models.Model):
    file_name=models.CharField(max_length=40, blank=True)
    file_path = models.CharField(max_length=1000, blank=True)
    def natural_key(self):
        return (self.file_name, self.file_path)
class Image_file(models.Model):
    file_name=models.CharField(max_length=40, blank=True)
    file_path = models.CharField(max_length=1000, blank=True)

    def natural_key(self):
        return (self.file_name, self.file_path)

class User_config(models.Model):
    user=models.ForeignKey(User)
    audio_file=models.ForeignKey(Audio_file)
    volume=models.FloatField(default=1)
    image_file=models.ForeignKey(Image_file, blank=True, null=True)
    transparent=models.FloatField(default=0.61)
    hex_color=models.CharField(default="#5bf9b6", max_length=7)