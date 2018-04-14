#conding = "utf-8"
from django.http import HttpResponseRedirect

def check(function):
    def check_inside(request,*args,**kwargs):
        if request.session.has_key("user_id"):
            return function(request,*args,**kwargs)
        else:
            fail = HttpResponseRedirect('/user/login/')
            fail.set_cookie("url",request.get_full_path())
            return fail
    return check_inside