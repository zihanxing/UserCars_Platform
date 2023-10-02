from AppBase.base import  *
from django.utils.decorators import method_decorator
from ShoppingApp import  models
from AppBase.models import AppMenuDict
from django.core import serializers
from django.contrib.auth import authenticate, login,logout
# Create your views here.
from django.db.models import Max
from django.utils import timezone

def redictIndex(request):
    #默认页面为配置中的第一项
    defaulturl="/shop/index"
    return  redirect(defaulturl)
# 主页
# @method_decorator(checkLogin, name='dispatch')
class IndexView(View):
    def get(self, request):

        #获取全部品牌
        brandList = models.GoodsRecord.objects.values("brand").order_by("brand").distinct()
        #获取全部车系
        modelList = models.GoodsRecord.objects.values("model").order_by("model").distinct()
        #获取全部排量
        volumeList = models.GoodsRecord.objects.values("volume").order_by("volume").distinct()
        # 获取变速箱
        gearboxList = models.GoodsRecord.objects.values("gearbox").order_by("gearbox").distinct()
        # 获取变速箱
        yearList = models.GoodsRecord.objects.values("year").order_by("year").distinct()

        ageList = models.GoodsRecord.objects.values("age").order_by("age").distinct()

        fuelList = models.GoodsRecord.objects.values("fuel").order_by("fuel").distinct()




        return render(request, "ShoppingApp/home.html",{"code": 200, "curUrl": "/ver/index","brandList":brandList,
                                                        "modelList":modelList,"volumeList":volumeList,"gearboxList":gearboxList,
                                                        "yearList":yearList,"ageList":ageList,"fuelList":fuelList })

class CarsListView(View):
    def get(self,request):
        #获取车辆信息列表
        searchName = request.GET.get("searchName", "")
        brand = request.GET.get("brand", "")
        model = request.GET.get("model", "")
        volume = request.GET.get("volume", "")
        gearbox = request.GET.get("gearbox", "")
        year = request.GET.get("year", "")
        age = request.GET.get("age", "")
        fuel = request.GET.get("fuel", "")
        maxprice = int(request.GET.get("maxprice", 0))
        minprice = int(request.GET.get("minprice", 0))

        minid = int(request.GET.get('curPage', 1))
        pagesize = request.GET.get('pageSize', 3)
        DataItems = models.GoodsRecord.objects.all()

        if brand !="":
            DataItems=DataItems.filter(Q(brand=brand))
        if volume !="":
            DataItems=DataItems.filter(Q(volume=volume))
        if gearbox !="":
            DataItems=DataItems.filter(Q(gearbox=gearbox))
        if year !="":
            DataItems=DataItems.filter(Q(year=year))
        if fuel != "":
            DataItems = DataItems.filter(Q(fuel=fuel))
        if maxprice > 0:
            DataItems = DataItems.filter(Q(price__lte=maxprice))
        if minprice > 0:
            DataItems = DataItems.filter(Q(price__gte=minprice))
        DataItems=DataItems[:100]#显示前20页
        pagInator = Paginator(DataItems, pagesize)  # 汽车数据分页处理
        currPage = pagInator.page(minid)  # 获取前端传入的第几页数据
        # 当前页的所有数据
        dataList = currPage.object_list
        data = []
        for item in dataList:
            data.append({"id": item.id, "name": item.name, "description": item.description,
                         "userName": item.creator.username,"goodsPic":item.pic.url,"price":str(item.price),"oldPrice":str(item.oldprice),
                         "userImage": item.creator.img.url,"brand":item.brand,"model":item.model,"volume":item.volume,"gearbox":item.gearbox
                         ,"year":item.year,"age":item.age,"mileage":item.mileage,"horsepower":item.horsepower,"torque":item.torque,"transfer_number":item.transfer_number
                         ,"fuel":item.fuel,"image":item.image})

        return successResponseCommon({"items": data, "pages": 1, "curpage": 1, "sumNum": len(DataItems),  "nodataflag": 1})

#商品列表
class GoodsListView(View):
    def get(self,request):
        #获取商品信息列表
        searchName = request.GET.get("searchKey", "")
        dataList = models.GoodsRecord.objects.filter(Q(name__contains=searchName)&Q(delete_flag=0))
        data = []
        for item in dataList:
            data.append({"id": item.id, "name": item.name, "description": item.description,
                         "userName": item.creator.username,"goodsPic":item.pic.url,"price":str(item.price),"oldPrice":str(item.oldprice),
                         "userImage": item.creator.img.url, "createTime": timeConverStr(item.create_time)})

        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": len(dataList),
             "nodataflag": 1})

#发布商品
@method_decorator(checkLogin, name='dispatch')
class AddGoodsView(View):
    def get(self, request):
        print('request.user', request.user.username)
        print('request.user', request.user.id)
        # 下面是判断是是否是匿名
        print('request.user', request.user.is_anonymous)
        username = request.user.username
        return render(request, "ShoppingApp/add_goods.html",{"code": 200})
    def post(self,request):
        #发布商品
        name=request.POST.get("name","")
        nums =int(request.POST.get("nums",0))
        brand = request.POST.get("brand", "")
        model = request.POST.get("model", "")
        volume = request.POST.get("volume", "")
        gearbox = request.POST.get("gearbox", "")
        oldprice = request.POST.get("oldprice", 0)
        price = request.POST.get("price", 0)
        year = request.POST.get("year", 0)
        age = request.POST.get("age", 0)
        mileage = request.POST.get("mileage", 0)
        horsepower = request.POST.get("horsepower", 0)
        torque = request.POST.get("torque", 0)
        transfer_number = request.POST.get("transfer_number", 0)
        fuel = request.POST.get("fuel", 0)
        description=""
        if request.FILES:
            pic = request.FILES.get('pic')
            goodRec=models.GoodsRecord(name=name,price=price,nums=nums,description=description,pic=pic,creator=request.user,
                                       brand=brand,  model=model,  volume=volume,  gearbox=gearbox,  oldprice=oldprice,
                                       year=year, mileage=mileage,  horsepower=horsepower,  torque=torque,  transfer_number=transfer_number,
                                       fuel=fuel,age=age
                                       )
        else:
            goodRec = models.GoodsRecord(name=name, price=price, nums=nums, description=description,creator=request.user,
                                         brand=brand, model=model, volume=volume, gearbox=gearbox, oldprice=oldprice,
                                         year=year, mileage=mileage, horsepower=horsepower, torque=torque,
                                         transfer_number=transfer_number,
                                         fuel=fuel,age=age
                                         )
        goodRec.save()
        goodRec.image=goodRec.pic.url
        goodRec.save()
        return successResponseCommon({}, "Successfully posted")

#我发布的商品
@method_decorator(checkLogin, name='dispatch')
class MyGoodsView(View):
    def get(self, request):
        return render(request, "ShoppingApp/my_goods.html", {"code": 200})


class MyGoodsDataView(View):
    def get(self, request):
        searchName = request.GET.get("searchKey", "")
        dataList = models.GoodsRecord.objects.filter(Q(creator=request.user)&Q(delete_flag=0)&Q(name__contains=searchName)&Q(nums=0))
        data = []
        for item in dataList:
            data.append({"id": item.id, "name": item.name, "description": item.description,"nums": str(item.nums),
                         "userName": item.creator.username, "goodsPic": item.pic.url, "price": str(item.price),
                         "oldPrice": str(item.oldprice),"fuel":str(item.fuel),"year":str(item.year),
                         "userImage": item.creator.img.url, "createTime": timeConverStr(item.create_time)})

        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": len(dataList),
             "nodataflag": 1})
    def delete(self,request):
        data=json.loads(request.body.decode("utf-8"),encoding="utf-8")
        id=data.get('id',0)
        dataitem = models.GoodsRecord.objects.get(id=id)
        dataitem.delete_flag = 1
        dataitem.save()
        return successResponseCommon({},"Successfully deleted！")
    def post(self,request):
        data = request.POST
        id = data.get('id', 0)
        name = data.get("name", "")
        price = data.get("price", 0)
        nums = int(data.get("nums", 0))
        description = data.get("description", "")
        dataitem = models.GoodsRecord.objects.get(id=id)
        dataitem.name=name
        if dataitem.price != price:
            dataitem.oldprice = dataitem.price
        dataitem.price = price
        dataitem.nums = nums
        dataitem.description = description
        if request.FILES:
            pic = request.FILES.get('pic')
            dataitem.pic=pic
        dataitem.save()
        return successResponseCommon({}, "Successfully modified!！")



#添加商品到收藏夹
class AddGoodsToCar(View):
    def post(self,request):
        data = request.POST
        id = data.get('id', 0)
        #根据id查询商品信息
        dataitem = models.GoodsRecord.objects.get(id=id)
        #查询购物车是否有此商品
        ShoppingCarList=models.ShoppingCar.objects.filter(Q(creator=request.user) & Q(goods=dataitem))
        if len(ShoppingCarList)>0:
            # ShoppingCarList.update(nums=F('nums') + 1)
            pass
        else:
            models.ShoppingCar.objects.create(goods=dataitem,nums=1,creator=request.user)
        return successResponseCommon({}, "Successfully collected！")



@method_decorator(checkLogin, name='dispatch')
#收藏夹
class ShoppingCarView(View):
    def get(self, request):
        return render(request, "ShoppingApp/shopping_cart.html", {"code": 200})
    def post(self,request):
        #收藏夹生成订单
        data = request.POST
        items = data.get('items', "")
        items=items.split('|')
        #计算
        costs= data.get('totalPrice',0)
        nums=data.get('totalNum',0)
        BillRecordMainrec=models.BillRecordMain.objects.create(costs=costs,nums=nums,creator=request.user)
        for item in items:
            if item!="":
                # 根据id查询收藏夹
                id=int(item)
                dataitem = models.ShoppingCar.objects.get(id=id)
                models.BillRecordSub.objects.create(main_rec=BillRecordMainrec,goods=dataitem.goods,nums=dataitem.nums,costs=dataitem.nums*dataitem.goods.price)
                dataitem.delete()
        return successResponseCommon({"id":BillRecordMainrec.id}, "Order created successfully")

class ShoppingCarDataView(View):
    def get(self, request):
        #查询当前用户的购物车信息
        dataList = models.ShoppingCar.objects.filter( Q(creator=request.user) )
        data = []
        for item in dataList:
            data.append({"id": item.id, "pro_name": item.goods.name, "pro_description": "车龄"+ str(item.goods.age)+"年", "pro_num": int(item.nums),
                          "pro_img": item.goods.image, "pro_price": float(item.goods.price),"pro_oldprice": float(item.goods.oldprice), "pro_year": str(item.goods.year)
                         })
        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": len(dataList),
             "nodataflag": 1})
    def delete(self,request):
        data = json.loads(request.body.decode("utf-8"), encoding="utf-8")
        id = data.get('id', 0)
        dataitem = models.ShoppingCar.objects.get(id=id)
        dataitem.delete()
        return successResponseCommon({}, "Successfully deleted!！")
    def post(self,request): #增加减少数量
        data = request.POST
        id = data.get('id', 0)
        nums = data.get('nums', 0)
        dataitem = models.ShoppingCar.objects.get(id=id)
        dataitem.nums=nums
        dataitem.save()
        return successResponseCommon({}, "Successfully modified!！")


class ShoppingBillDetailView(View):
    def get(self,request):
        id= request.GET.get("id", 0)
        BillRecordMainrec = models.BillRecordMain.objects.get(id=id)
        return render(request, "ShoppingApp/bill_detail.html", {"billId": id,"bill_status":BillRecordMainrec.bill_status})


class ShoppingBillDetailDataView(View):
    def get(self, request):
        id = request.GET.get("id", 0)
        BillRecordMainrec = models.BillRecordMain.objects.get(id=id)
        #获取订单详情数据
        dataList = models.BillRecordSub.objects.filter(Q(main_rec=BillRecordMainrec))
        data = []
        for item in dataList:
            data.append({"id": item.id, "pro_name": item.goods.name, "pro_description":"车龄"+ str(item.goods.age)+"年",
                         "pro_num": int(item.nums),
                         "pro_img": item.goods.image, "pro_price": float(item.goods.price),
                         })
        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": len(dataList),
             "nodataflag": 1})
    def post(self,request): #pay
        data = request.POST
        id = data.get('id', 0)
        dataitem = models.BillRecordMain.objects.get(id=id)
        dataitem.bill_status="Successfully paid"
        dataitem.save()
        return successResponseCommon({}, "Successfully modified!！")



#我的订单
class MyBillsView(View):
    def get(self, request):
        return render(request, "ShoppingApp/my_bills.html", {"code": 200})


class MyBillsDataView(View):
    def get(self, request):
        searchName = request.GET.get("searchKey", "")
        dataList = models.BillRecordMain.objects.filter(Q(creator=request.user))

        data = []
        for item in dataList:
            #查询商品明细
            BillRecordSub=models.BillRecordSub.objects.filter(Q(main_rec=item))
            data.append({"id": item.id,  "name": str(BillRecordSub[0].goods.name),
                         "price": str(item.costs),
                         "bill_status": str(item.bill_status),
                          "createTime": timeConverStr(item.create_time)})

        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": len(dataList),
             "nodataflag": 1})

    def delete(self, request):
        data = json.loads(request.body.decode("utf-8"), encoding="utf-8")
        id = data.get('id', 0)
        dataitem = models.BillRecordMain.objects.get(id=id)
        dataitem.delete()
        return successResponseCommon({}, "Successfully deleted!！")


class CreateMyBillsView(View):
    def post(self,request):
        #收藏生成订单
        data = request.POST
        id = data.get('id', "")
        #查询商品
        goodsitem=models.GoodsRecord.objects.get(id=id)
        #计算
        costs= goodsitem.price
        nums=1
        BillRecordMainrec=models.BillRecordMain.objects.create(costs=costs,nums=nums,creator=request.user)
        models.BillRecordSub.objects.create(main_rec=BillRecordMainrec,goods=goodsitem,nums=nums,costs=costs)
        return successResponseCommon({"id":BillRecordMainrec.id}, "Order created successfully！")

def valuationPage(request):
    return render(request, 'ShoppingApp/valuation.html')


def valuation(request):
    result = 0
    if request.POST:
        brand = request.POST['brand']
        gearbox = request.POST['gearbox']
        if gearbox == 'automatic':
            gearbox = 1
        else:
            gearbox = 0
        fuel = request.POST['fuel']
        if fuel == 95:
            fuel = 1
        else:
            fuel = 0
        age = float(request.POST['age'])
        oriPrice = float(request.POST['oriPrice'])
        volume = float(request.POST['volume'])
        mileage = float(request.POST['mileage'])
        transferTime = float(request.POST['transferTimes'])
        if brand == 'AUDI':
            result = 0.803965 + 0.046115 * volume - 0.001733 * oriPrice - 0.052994 * age - 0.003420 * mileage
        elif brand == 'BENZ':
            result = 0.8989121 + 0.0107207 * volume + 0.0001136 * oriPrice - 0.0658394 * age - 0.0035155 * mileage
        elif brand == 'BMW':
            result = 0.872949 + 0.069073 * volume - 0.003289 * oriPrice - 0.059462 * age - 0.004333 * mileage - 0.002138 * transferTime
        elif brand == 'BUICK':
            result = 0.601765 + 0.601765 * volume + 0.001736 * oriPrice - 0.053136 * age - 0.003141 * mileage + 0.066065 * fuel
        elif brand == 'CHEVROLET':
            result = 0.747205 + 0.026362 * gearbox - 0.005416 * oriPrice - 0.0431016 * age - 0.003490 * mileage - 0.002206 * transferTime + 0.078880 * fuel
        elif brand == 'VOLKSWAGEN':
            result = 0.696092 + 0.095162 * volume + 0.039314 * gearbox - 0.006669 * oriPrice - 0.043438 * age - 0.005507 * mileage + 0.045181 * fuel
        elif brand == 'FORD':
            result = 0.6381207 + 0.0459592 * volume + 0.0294804 * gearbox + 0.0004712 * oriPrice - 0.0474148 * age - 0.0047237 * mileage
        elif brand == 'HAVAL':
            result = 0.932931 + 0.046702 * volume + 0.033629 * gearbox - 0.015100 * oriPrice - 0.064489 * age - 0.003311 * mileage
        elif brand == 'HONDA':
            result = 0.930084 + 0.026889 * volume - 0.001646 * oriPrice - 0.055168 * age - 0.002888 * mileage
        elif brand == 'GEELY':
            result = 0.885511 + 0.019397 * volume + 0.055257 * gearbox - 0.011575 * oriPrice - 0.063640 * age - 0.004872 * mileage
        elif brand == 'KIA':
            result = 0.744763 + 0.056908 * volume + 0.062633 * gearbox - 0.009506 * oriPrice - 0.043642 * age - 0.003822 * mileage
        elif brand == 'MAZDA':
            result = 0.836188 + 0.046210 * volume + 0.046210 * gearbox - 0.006978 * oriPrice - 0.055420 * age - 0.002419 * mileage
        elif brand == 'NISSAN':
            result = 0.732438 + 0.034592 * volume + 0.056803 * gearbox - 0.001502 * oriPrice - 0.044957 * age - 0.003995 * mileage - 0.031267 * fuel
        elif brand == 'TOYOTA':
            result = 0.830629 + 0.017552 * gearbox + 0.004386 * oriPrice - 0.051709 * age - 0.004279 * mileage + 0.017537 * fuel
        elif brand == 'HYUNDAI':
            result = 0.796672 + 0.026275 * volume + 0.052655 * gearbox - 0.007179 * oriPrice - 0.007179 * age - 0.004095 * fuel
        if result >= oriPrice:
            result = oriPrice * 0.9
        if result < 0:
            result = 0.5
        return render(request, "ShoppingApp/valuationResult.html", context={'data': round(oriPrice * result * 10000, 2)})