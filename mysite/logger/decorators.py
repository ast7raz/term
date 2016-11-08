from django.contrib.auth.models import User
import json
from models import Logger_Action
def Added_action_terminal(fun):
    def wraper_added(request, *args, **kwargs):
        req_slov=json.loads(request.body)
        user = User.objects.get(id=request.session.__getitem__('_auth_user_id'))

        for i in req_slov["ids"]:

            Logger_Action.objects.create(user=user, action_name=req_slov["command"], object_name="Terminal", object=i)
        #pass
        return fun(request)


    return wraper_added
def Added_action_of_post(fun):
    def wraper_added(request, *args, **kwargs):
        user = User.objects.get(id=request.session.__getitem__('_auth_user_id'))
        if request.method == "POST":
            page=request.POST["page"].split("/")

            response=fun(request)
            Logger_Action.objects.create(user=user, action_name=page[-1], action=response.content, object_name="Terminal", object=page[-2])
            return response

    return wraper_added