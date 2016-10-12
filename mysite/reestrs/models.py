# -*- coding: utf-8 -*-
from django.db import models
from social.apps.django_app.default.models import UserSocialAuth
from phonebook.models import Partner, Club, Cash,Roll
class Request_Instrument(models.Model):
    instrument=models.CharField(max_length=20)
    def __unicode__(self):
        return unicode(self.instrument)
class Request_type(models.Model):
    request_type=models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.request_type)
class Request_subject(models.Model):
    subject=models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.subject)
class Request_state(models.Model):
    name=models.CharField(max_length=30)
    def __unicode__(self):
        return unicode(self.name)


class Request_Reestr(models.Model):
    time=models.DateTimeField(auto_now_add=True, editable=False)
    user=models.ForeignKey(UserSocialAuth)
    partner=models.ForeignKey(Partner)
    partname=models.CharField(max_length=300, blank=True)
    club=models.ForeignKey(Club, null=True, blank=True)
    clubname=models.CharField(max_length=100, blank=True)
    cash=models.ForeignKey(Cash, null=True, blank=True)
    cashname=models.CharField(max_length=20, blank=True)
    instrument=models.ForeignKey(Request_Instrument)
    user_position=models.ForeignKey(Roll)
    request_type=models.ForeignKey(Request_type)
    request_subject=models.ForeignKey(Request_subject)
    coment=models.CharField(max_length=500)
    duration=models.IntegerField()
    otrs_ticket=models.CharField(max_length=20, blank=True)
    jira_BUG=models.CharField(max_length=10, blank=True)
    request_level=models.IntegerField(blank=False, default=1)
    state=models.ForeignKey(Request_state)

    def __unicode__(self):
        if self.cash:
            pa=self.cash
        elif self.club:
            pa=self.club
        elif self.partner:
            pa=self.partner
        ls=[unicode(self.time), unicode(self.user), unicode(pa), unicode(self.user_position.roll_name), unicode(self.coment)]
        return unicode(u"; ".join(ls))

    def Create_In_Form(self, obj):

        """for key in obj:
            print("%s = %s" %(unicode(key), unicode(obj[key])))"""
        if obj["priz"]==u"part":
            objcash=None
            objclub=None
            objpartner=Partner.objects.get(id=obj["cash_id"])
            cashname=''
            clubname=''
            partname=objpartner.part_name

            #print(objpartner)
        elif obj["priz"]=="cash":
            objcash=Cash.objects.get(id=obj["cash_id"])
            objclub=objcash.club
            objpartner=objcash.partner
            cashname=objcash.cash_name
            clubname=objclub.club_name
            partname=objpartner.part_name
            #print(objcash.partner.part_name)
        if obj["username"]=="astadmin":
            username="asorokin"
        else:
            username=obj["username"]
        objuser=UserSocialAuth.objects.get(user__username=username)
        if obj["otrs"]!='':
            objstate=Request_state.objects.get(name=u"Открыт")
        else:
            objstate=Request_state.objects.get(name=u"Закрыт")
        print("Proba")
        obj2=Request_Reestr(
                            user=objuser,
                            partner=objpartner,
                            partname=partname,
                            club=objclub,
                            clubname=clubname,
                            cash=objcash,
                            cashname=cashname,
                            instrument_id=int(obj["instrument"]),
                            user_position_id=int(obj["usposition"]),
                            request_type_id=int(obj["requesttype"]),
                            request_subject_id=int(obj["requestsubj"]),
                            coment=obj["coment"],
                            duration=int(obj["duration"]),
                            otrs_ticket=obj["otrs"],
                            jira_BUG=obj["jira"],
                            request_level=obj["level"],
                            state=objstate,
        )
        #print("Proba2")
        return obj2
# Create your models here.
