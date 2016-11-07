from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from models import User_Sessions
def set_user_online(fun):
    def wraper_seter(request, *args, **kwargs):
        #print(request.COOKIES["sessionid"])
        user=User.objects.get(id=request.session.__getitem__('_auth_user_id'))
        session=Session.objects.get(session_key=request.COOKIES["sessionid"])
        us=User_Sessions.objects.get_or_create(user=user, session=session)
        #us.save()
        #print(us)
        return fun(request)
        #print("onliner end")

    return wraper_seter