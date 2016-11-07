from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
# Create your models here.
class User_Sessions(models.Model):
    user=models.ForeignKey(User)
    session=models.ForeignKey(Session)
    def delete(self,*args, **kwargs):
        Session.objects.get(session_key=self.session.session_key).delete()
        print(self.session.session_key)

        #super(User_Sessions, self).delete(*args, **kwargs)



    def __unicode__(self):
        return ("%s - %s  |  %s" %(self.user.username, self.session.session_key, self.session.expire_date))