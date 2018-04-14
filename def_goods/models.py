from django.db import models
from tinymce.models import HTMLField

# Create your models here.

# 商品分类
class TypeInfo(models.Model):
    tname=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.tname

#
class GoodsInfo(models.Model):
    gname=models.CharField(max_length=20)
    gpic = models.ImageField(upload_to="def_goods")
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gdanwei = models.CharField(max_length=20,default="500g")
    gclick = models.IntegerField()      # 点击量
    gjianjie = models.CharField(max_length=250)
    gdescribe = HTMLField(max_length=1000)   # 商品详细介绍
    gkucun = models.IntegerField()      # 库存量
    gtype = models.ForeignKey(TypeInfo)# TypeInfo 要加“”
