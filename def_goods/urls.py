from django.conf.urls import url
from . import views
urlpatterns = [
    # 首页
    url(r'^index',view=views.index,name="index"),
    url(r'^list(\d+)_(\d+)_(\d+)/',views.list,name='list'), # typeid Pindex  sort = "1" 默认id
    # 商品详情页
    url(r'^(\d+)/',views.detail,name="detail"),
    url(r"^search/",views.mysearch())
]