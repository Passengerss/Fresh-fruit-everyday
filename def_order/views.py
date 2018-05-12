from django.shortcuts import render,redirect
from .models import OrderInfo,OrderDetail
from def_user.models import UserInfo
from def_car import models
from django.db import transaction
from datetime import datetime

def order(request):
    user_id = request.session["user_id"]
    user = UserInfo.objects.get(id=user_id)
    car_ids = request.GET.getlist("car_id")[:-1] # 拼接时最后一个为空不要
    cars = []
    for car in car_ids:
        cars.append(models.CarInfo.objects.get(id=car))
    context = {
        "title":"订单提交",
        "user":user,
        "cars":cars,
        "car_ids":car_ids
    }
    return render(request,"def_order/place_order.html",context)

# 订单处理
"""
事务：一旦操作失败,则全部回退
1,创建订单对象
2，判断商品库存
3，创建详细订单对象
4，修改商品库存
5，删除购物车
"""
# 创建事务，用装饰器
@transaction.atomic()
def order_handle(request):
    tran_id = transaction.savepoint() # 保存一个点，做回退的起点
    # 接受购物车编号
    car_ids = request.GET.getlist("car_id")[:-1]
    try:
        # 创建订单对象
        order = OrderInfo()
        now = datetime.now()
        uid = request.session["user_id"]
        order.water_number= "%s%d"%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.buyer_id = uid
        order.date_time = now
        order.total_count = request.GET.get("total")
        order.total_money = request.GET.get("money")
        order.address = UserInfo.objects.get(id=uid).uaddress
        order.save()
        # 创建订单详表
        ids = [int(item) for item in car_ids]
        for id1 in ids:
            detail = OrderDetail()
            detail.order=order
            # 查询购物车对应id的那一条信息
            cart = models.CarInfo.objects.get(id=id1)
            goods = cart.goods
            if goods.gkucun>=cart.count:    # 如果库存大于购买数量
                # 减少商品库存
                goods.gkucun -= cart.count
                goods.save()
                # 完善订单信息
                detail.goods_id = goods.id  # detail.goods
                detail.goods_name = goods.gname
                detail.goods_price = goods.gprice
                detail.goods_count = cart.count
                detail.save()
                cart.delete()
            else:
                transaction.savepoint_rollback(tran_id)# 回滚操作
                return  redirect("car:car")
        transaction.savepoint_commit(tran_id)
    except Exception as e:
        print("========OrderHandle=======%s"%e)
        transaction.savepoint_rollback(tran_id)# 回滚操作
    return redirect("user:user_center_order")