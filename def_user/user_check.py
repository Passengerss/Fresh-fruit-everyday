#conding = "utf-8"
from django.http import HttpResponseRedirect
from django.urls import reverse

def check(function):
    def check_inside(request,*args,**kwargs):
        if request.session.has_key("user_id"):
            return function(request,*args,**kwargs)
        else:
            fail = HttpResponseRedirect(reverse('user:login',args=()))
            fail.set_cookie("url",request.get_full_path())
            return fail
    return check_inside