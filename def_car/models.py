from django.db import models

# 购物车模型

class CarInfo(models.Model):
    user = models.ForeignKey("def_user.UserInfo")
    goods = models.ForeignKey("def_goods.GoodsInfo")
    count = models.IntegerField(default=1)      # 保存同一个商品的数量
