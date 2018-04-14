from django.shortcuts import render,redirect
from def_user import user_check
from .models import *
from django.http import JsonResponse


# 购物车
@user_check.check
def car(request):
    uid = request.session["user_id"]
    cars = CarInfo.objects.filter(user_id=uid)  # 表格中总共多少条该用户数据
    context = {"title":"购物车","cars":cars}
    tmp = render(request,'def_car/cart.html',context)
    # 后退时浏览器自动刷新
    tmp.setdefault('Cache-Control', 'no-store')
    tmp.setdefault('Expires', 0)
    tmp.setdefault('Pragma', 'no-cache')
    return tmp

# 立即购买
# 加入购物车
@user_check.check
def add_to_car(request,gid,gcount):
    # 传入商品ID，商品数量
    uid = request.session["user_id"]
    gid = int(gid)
    gcount = int(gcount)
    if gid!=0 and gcount==0:    # 购买数量为0，属于无效数据
        return
    else:
        if gid == 0 and gcount == 0:    # index,list,detail 无参数查询刷新数据，
            # count_of_data = CarInfo.objects.filter(user_id=uid).count() # 查看该用户有多少条数据
            count_of_data = CarInfo.objects.filter(user_id=uid)  # 查看所有商品总数
            count = []
            for each in count_of_data:
                count.append(each.count)
            count = sum(count)
            return JsonResponse({"uid": uid, "gid": gid, "count": count,})
        else:
            # 查询购物车是否有此商品，如果有则数量增加，如果无则新增
            cars = CarInfo.objects.filter(user_id=uid, goods_id=gid)
            if len(cars) >= 1:
                goods_in_car = cars[0]
                goods_in_car.count += gcount
                goods_in_car.save()
            else:
                car = CarInfo()
                car.user_id = uid
                car.goods_id = gid
                car.count = gcount
                car.save()
            # count_of_data = CarInfo.objects.filter(user_id=uid).count() # 查看该用户有多少条数据
            count_of_data = CarInfo.objects.filter(user_id=uid) # 查看所有商品总数
            count=[]
            for each in count_of_data:
                count.append(each.count)
            count = sum(count)
            return JsonResponse({"uid":uid,"gid":gid,"count":count})

# 购物车的修改
def change(request,car_id,count):
    # 传入商品在购物车id，商品数量
    try:
        car = CarInfo.objects.get(id=car_id)
        car.count=int(count)
        car.save()
        return JsonResponse({"status":1})
    except Exception:
        return JsonResponse({"status":0})

#
def delete(request,car_id):
    try:
        car = CarInfo.objects.get(id=int(car_id))
        print(car)
        car.delete()
        return JsonResponse({"status": 1})
    except Exception:
        return JsonResponse({"status": 0})


