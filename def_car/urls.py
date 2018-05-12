from django.conf.urls import url
from . import views

urlpatterns=[
    # 购物车
    url(r'^info/car/$',views.car,name="car"),
    # 添加到购物车
    url(r'^add_to_car(\d+)_(\d+)/$',view=views.add_to_car,name="add_to_car"),
    # 修改购物车数据
    url(r"^change(\d+)_(\d+)/$",views.change,name="change"),
    # 删除购物车数据
    url(r"^delete(\d+)/$",views.delete,name="delete")
]
