# -*- coding: utf-8 -*-
from django.db import models
from phonebook.models import Partner, Club

class Parser_users(models.Model):
    username=models.CharField(max_length=40)
    userpass=models.CharField(max_length=40)
    parser=models.CharField(max_length=20)
    parsurl=models.CharField(max_length=100, blank=True, default="")
    pars_proxy=models.CharField(max_length=25, blank=True, default="")
    def __unicode__(self):
	return unicode(self.parser)

class Keys(models.Model):
    key=models.CharField(max_length=45)
    name=models.CharField(max_length=40, blank=True)
    part=models.ForeignKey(Partner)
    club=models.ForeignKey(Club)
    admin=models.CharField(max_length=40,blank=True, default="")
    pas=models.CharField(max_length=40,blank=True)
    ip=models.IPAddressField(blank=True, default="")
    version=models.CharField(max_length=40,blank=True, default="")
    base_id=models.IntegerField(blank=True, null=True)
    active=models.BooleanField(default=False)
    blocked=models.BooleanField(default=False)
    machine_id=models.CharField(max_length=35, blank=True, default="")
    date_last_online=models.CharField(max_length=20, blank=True, default="")
    class Meta:
	permissions=(
	("Averange", "Averange"),)
    def __unicode__(self):
        return unicode(self.key)
    def create_in_dict(self, dict_key):
        #print(u"Начало проверок")
        if type(dict_key["part"])!=object:
            #print("Hi")
            try:
                part=Partner.objects.get(part_name=dict_key["part"])
                print("Partner exist")
            except:
                part=Partner(part_name=dict_key["part"])
                part.save()
                print("Partner saved ")
            #print(part)
            self.part=part
        else:
            self.part=dict_key["part"]
        if type(dict_key["club"])!=object:
            #print("Hi")
            try:
                club=Club.objects.get(club_name=dict_key["club"])
                print("Club exist ")
            except:
                club=Club(club_name=dict_key["club"], partner=self.part)
                club.save()
                print("Club saved ")
            self.club=club
        else:
            self.club=dict_key["club"]
        self.key=dict_key["key"]
        self.name=dict_key["name"]
        self.admin=dict_key["admin"]
        #print(self.admin)
        self.pas=dict_key["pas"]
        try:
            self.ip=dict_key["ip"]
        except:
            self.ip=""
        try:
            self.version=dict_key["version"]
        except:
            self.version=""
        #print(self.key)
        #print(self.name)
        #print(self.admin)
        #print(self.pas)
        #print(self.part)
        #print(self.club)
        #self.ip=None
        #self.version=None"""
        return self
        
    """def save(self):
        #print(self.part)

        partner=Partner.objects.filter(part_name=self.part)

        if len(partner)==0:
            #print(partner)
            pa=Partner(part_name=self.part)
            pa.save()
            print("save "+self.part)
            partner=Partner.objects.filter(part_name=self.part)
        #print(partner)
        clubs=Club.objects.filter(club_name=self.club)
        if len(clubs)==0:
            #print(clubs)
            cl=Club(club_name=self.club, partner=partner[0])
            cl.save()
            print("save "+self.club)
            clubs=Club.objects.filter(club_name=club)
        #print(clubs[0])
        self.part=partner[0]
        self.club=clubs[0]
        #print(self.clean())
        super(Keys, self).save()
        if len(partner)==0:
            obj1=Partner()
            obj1.save(part_name=slov["part"])
        partner=Partner.Object.get(slov["part"])
        clube=Club.Object.get(club_name=slov["clube"])
        if len(clube)==0:
            Club.save(club_name=slov["clube"], partner=slov["part"])

        super(Keys, self).save(slov)
"""
# Create your models here.
