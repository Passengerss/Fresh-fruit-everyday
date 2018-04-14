"""Fruitstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from def_goods.views import index
urlpatterns = [
    url(r"^$",view=index),
    url(r'^admin/', admin.site.urls),
    url(r'^user/',include('def_user.urls',namespace="")),
    url(r'^user/',include('def_goods.urls',namespace="user")),
    url(r"^car/",include("def_car.urls",namespace="car")),
    url(r"^order/",include("def_order.urls",namespace="order")),
    url(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    #url(r'^search/',include("haystack.urls")),  # 全文检索，自定义上下文时，需要到应用里直接调用视图
]
