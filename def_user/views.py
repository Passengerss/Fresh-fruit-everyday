#coding=UTF-8
from django.shortcuts import render,redirect
from .models import UserInfo
from hashlib import sha1
from django.urls import reverse
from django.http import HttpResponseRedirect
from .user_check import check
from def_order import models
from django.http import JsonResponse

# Create your views here.

# 注册界面
def register(request):
    context = {"title":"注册"}
    return render(request,'def_user/register.html',context=context)

# 退出登录
def loginout(request):
    request.session.flush( )
    return redirect('goods:index')

# 处理注册信息
def register_handle(request):
    # 接受用户输入
    post = request.POST
    uname = post.get("user_name")
    upwd = post.get("pwd")
    upwd2 = post.get("cpwd")
    uemail = post.get("email")
    # 判断两次密码
    if upwd != upwd2:
        redirect('user:register')

    # sha1加密
    s1 = sha1()
    s1.update(upwd.encode())
    upwd3 = s1.hexdigest()

    # 创建模型类对象，保存到数据库
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，转到登录页面
    return redirect('user:login')

#
def register_exist(request,username):
    YoN = UserInfo.objects.filter(uname=username)
    if len(YoN) == 1:
        return JsonResponse({"status":1})   # 用户名不存在
    else:
        return JsonResponse({"status":0})


def login(request):
    uname = request.COOKIES.get("user_name",'')
    context = {"title":"用户登录","error_name":0,"error_pwd":0,"uname":uname}
    return render(request,'def_user/login.html',context=context)

def login_handle(request):

    ''' 处理登录信息，会话状态'''
    uname = request.POST.get("username")
    upwd = request.POST.get("pwd")
    remember = request.POST.get("remember",0) # 记住服务为1
    # 根据数据模型查数据，判断登录信息是否正确
    users = UserInfo.objects.filter(uname=uname)

    # 如果用户名无错误，则判断密码是否正确
    if len(users):
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        if s1.hexdigest() == users[0].upwd:
            print("=========================>密码正确")
            # 读取用户开始访问的url
            #success = HttpResponseRedirect(request.COOKIES["url"])
            success = HttpResponseRedirect(reverse("goods:index",args=()))   # redirect 不能保存cookies。这个可以
            #记住密码
            if remember:
                success.set_cookie(key="user_name",value=uname.encode('utf-8').decode("iso-8859-1"))
            else:
                success.set_cookie("user_name",'',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return  success

        else:#密码错误
            context = {"title": "用户登录", "error_name": 0, "error_pwd": 1, 'uname': uname, 'upwd': upwd}
            return render(request, 'def_user/login.html', context=context)
    else:
        context = {"title":"用户登录","error_name":1,"error_pwd":0,'uname':uname,'upwd':upwd}
        return render(request,'def_user/login.html',context=context)

# 用户中心
@check
def user_center_info(request):
    # 名字在login_handle中有存session
    user_name = request.session["user_name"]
    Objects = UserInfo.objects.get(id=request.session["user_id"])
    uemail = Objects.uemail
    context = {"title":"个人信息","name":user_name,'email':uemail,"Objects":Objects}
    return render(request,'def_user/user_center_info.html',context=context)

# 用户订单
@check
def user_center_order(request):
    order_detail = models.OrderDetail
    user_id = request.session.get("user_id")
    infos = models.OrderInfo.objects.filter(buyer_id=user_id)
    dict_data = {}   # {"info:detail","":[]}
    for each in infos:
        dict_data[each] = order_detail.objects.filter(order_id=each.id)

    context = {"title":"订单","infos":infos,"dict_data":dict_data}
    return render(request,'def_user/user_center_order.html',context)

# 用户地址
@check
def user_center_site(request):
    user = UserInfo.objects.get(uname=request.session['user_name'])
    if request.method == "POST":
        user.urecieve = request.POST.get('urecieve')
        user.uaddress = request.POST.get('uaddress')
        user.uyoubian = request.POST.get('uyoubian')
        user.uphone = request.POST.get('uphone')
        user.save()
    context = {"title":"地址","user":user}
    return  render(request,'def_user/user_center_site.html',context=context)



