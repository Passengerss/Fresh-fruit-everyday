from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','tname']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gname','gprice','gclick','gkucun','gjianjie','gdescribe','isDelete','gtype']
    #设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'gname')
    list_filter = ["id","gname","gprice","gclick","isDelete"]
    search_fields = ["gname","gjianjie","gdescribe"]
# admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
#
admin.site.site_header="天天生鲜后台资源管理系统" # 此处设置页面显示标题
admin.site.site_title="天天生鲜后台管理"  # 此处设置页面头部标题


