from django.shortcuts import render
from .models import *
from django.core.paginator import *
# Create your views here.

# 首页
def index(request):
    # 查询各分类的最新四条数据，最热四条数据

    # dict_new = {}   # 最新数据  {0:[]}
    # dict_hot = {}   # 热门数据  {0:[]}
    # # pack_data = {}  # 打包数据  {0:{new:dict_new,hot:dict_hot}}
    # # pack_data=pack_data.fromkeys(range(6),{})   #{0:{new:{0:[]},hot:{0:[]}}}
    # # 类型按typelist从0开始{0:[]}
    # for number,type_name in enumerate(typelist):
    #     dict_new[number] = type_name.goodsinfo_set.order_by('-id')[0:4]   # 最新的id最大，所以倒序排序
    #     dict_hot[number] = type_name.goodsinfo_set.order_by('-gclick')[0:4] # 获取热度最高的四条
    #     # pack_data[number]["new"] = dict_new
    #     # pack_data[number]["hot"] = dict_hot

    typelist = TypeInfo.objects.all()  # 获取所有
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]   # 最新的id最大，所以倒序排序
    type00 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]  # 最新的id最大，所以倒序排序
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]  # 最新的id最大，所以倒序排序
    type22 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]  # 最新的id最大，所以倒序排序
    type33 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]  # 最新的id最大，所以倒序排序
    type44 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]  # 最新的id最大，所以倒序排序
    type55 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]  # 获取热度最高的四条
    context = {"title":"首页",
               "typelist":typelist,
               "type0":type0,"type00":type00,
               "type1":type1,"type11":type11,
               "type2":type2,"type22":type22,
               "type3":type3,"type33":type33,
               "type4":type4,"type44":type44,
                "type5":type5,"type55":type55,
               }
    return render(request,'def_goods/index.html',context=context)

# 商品列表页
# 对应参数功能
def list(reuqest,type_id,page_index,sort_by):
    typeinfo = TypeInfo.objects.get(id=int(type_id))
    news = typeinfo.goodsinfo_set.order_by("-id")[0:2]
    if sort_by == '1': # 默认·最新
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by("-id")
    elif sort_by == "2": # 根据价格
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by("-gprice")
    elif sort_by == "3": # 根据人气·点击量
        goods_list = GoodsInfo.objects.filter(gtype_id=int(type_id)).order_by("-gclick")
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(page_index))  # 返回某一页所有对象
    context = {
        'title':"商品列表",
        "ttitle":typeinfo.tname,
        'guest_cart':1,
        'page':page,
        "paginator":paginator,
        "typeinfo":typeinfo,
        'sort':sort_by,
        'news':news,
    }
    return render(request=reuqest,template_name='def_goods/list.html',context=context)

# 商品详情页
def detail(request,goods_id):
    goods = GoodsInfo.objects.get(id=int(goods_id))
    goods.gclick+=1
    goods.save()
    news = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'title':'商品详情',
        'ttitle':goods.gtype.tname,
        'guest_cart':1,
        'goods':goods,
        'news':news,
        'id':goods_id,
    }
    #response = render(request,"def_goods/detail.html",context)

    # 代码实现有问题
    ''' 
    # 记录最近浏览，在用户中心展示
    goods_ids = request.COOKIES.get("goods_ids",'')
    goods_id_ = '%d'%goods.id
    if goods_ids != "": # 判断是否有浏览记录，如果有则继续判断
        goods_ids1 = goods_ids.split(',') # 拆分为列表
        if goods_ids1.count(goods_id_) > 1:  # 如果商品已经被记录，则删除
            goods_ids1.remove(goods_id_)
            goods_ids1.insert(0,goods_id_) # 添加到第一个
        if len(goods_ids1) >= 6:   # 如果超过6个，则删除最后一个
            del goods_ids1[5]
        goods_ids = ",".join(goods_ids1) # 拼接为字符串
    else:
        goods_ids = goods_id_ # 如果没有浏览记录则直接记录
    response.set_cookie("goods_ids",goods_ids)  # 写入cookie
    '''
    return render(request,"def_goods/detail.html",context)

# 全文检索的自定义上下文
from haystack.views import SearchView
class mysearch(SearchView):
    def extra_context(self):
        context = super(mysearch,self).extra_context()
        context["title"] = "搜索"
        return context