from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # class Meta():
    #   db_table = "UserInfo" # 不然数据库名字会是：应用名_数据库名
    # xxx = models.CharField(db_column="字段名")  # 可以独立设置数据库中的字段
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40) # 采用sha1加密
    uemail = models.CharField(max_length=30)
    urecieve = models.CharField(max_length=20,default="")   # 联系地址
    uaddress = models.CharField(max_length=200,)    # 收件人地址
    uyoubian = models.CharField(max_length=6,default="")
    uphone = models.CharField(max_length=11,default="")