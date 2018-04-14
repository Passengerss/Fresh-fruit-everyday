from django.conf.urls import url
from . import views
urlpatterns = [
    # 注册
    url(r'^register/$',view=views.register),
    url(r'^register_handle/$',view=views.register_handle),
    # 验证注册
    url(r"^register_exist/(\w+)/$",views.register_exist),
    # 登录
    url(r'^login/$',view=views.login),
    url(r'^login_handle',view=views.login_handle),
    # 用户中心
    url(r'^info/$',view=views.user_center_info ),
    # 订单
    url(r'^info/user_center_order',views.user_center_order),
    # 地址
    url(r'^info/user_center_site',views.user_center_site),
    # 退出登录
    url(r'^loginout',view=views.loginout),

]