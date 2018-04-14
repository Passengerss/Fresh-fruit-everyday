from django.db import models

# 订单基本信息
class OrderInfo(models.Model):
    # 无支付方式，物流信息
    buyer = models.ForeignKey("def_user.UserInfo")
    water_number = models.CharField(max_length=20)    # 订单编号
    pay_or_not = models.BooleanField(default=False) # 是否支付
    # pay_way = models.ForeignKey("PayWay")   # 支付方式
    date_time=models.DateTimeField(auto_now=True)
    total_count = models.IntegerField(default=0)   # 总数量
    total_money = models.DecimalField(max_digits=6,decimal_places=2) # 总金额
    address = models.CharField(max_length=200)
    class Meta():
        db_table = "OrderInfo"

# 订单详情
class OrderDetail(models.Model):
    goods = models.ForeignKey("def_goods.GoodsInfo")
    order = models.ForeignKey("Orderinfo")
    goods_name = models.CharField(max_length=20)
    goods_price = models.DecimalField(max_digits=5,decimal_places=2)
    goods_count = models.IntegerField()
    # 用JS完成小计计算
    class Meta():
        db_table = "OrderDetail"

# 支付方式
class PayWay(models.Model):
    #Alipay = models.CharField(max_length=6)
    class Meta():
        db_table = "PayWay"