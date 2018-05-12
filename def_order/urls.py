from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$",view=views.order,name="order"),
    url(r"^handle/$",views.order_handle,name="order_handle")
]