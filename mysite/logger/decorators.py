from django.contrib.auth.models import User
import json
from models import Logger_Action
from ipware.ip import get_ip
def Added_action_terminal(fun):
    def wraper_added(request, *args, **kwargs):
        req_slov=json.loads(request.body)
        user = User.objects.get(id=request.session.__getitem__('_auth_user_id'))
        #ip=request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
	ip=get_ip(request,
		 right_most_proxy=True,
		 #real_ip_only=True,
		 )
        for i in req_slov["ids"]:

            Logger_Action.objects.create(user=user, action_name=req_slov["command"], object_name="Terminal", object=i, user_ip=ip)
        #pass
        return fun(request)


    return wraper_added
def Added_action_of_post(fun):
    def wraper_added(request, *args, **kwargs):
        user = User.objects.get(id=request.session.__getitem__('_auth_user_id'))
        if request.method == "POST":
            page=request.POST["page"].split("/")
            #ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
            ip = get_ip(request, real_ip_only=True) or "127.0.0.1"
            response=fun(request)
            Logger_Action.objects.create(user=user, action_name=page[-1], action=response.content, object_name="Terminal", object=page[-2],user_ip=ip)
            return response

    return wraper_added