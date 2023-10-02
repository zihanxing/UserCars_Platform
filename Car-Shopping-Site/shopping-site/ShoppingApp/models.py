from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.
from AppBase.models import  UserDict


class Car(models.Model):
    id = models.AutoField(primary_key=True)  # 自定义自增列
    #新增属性 品牌  车系  排量  变速箱   年份 车龄 公里数  扭矩  马力  转手次数  汽油  图片
    brand = models.CharField(max_length=20, blank=True, null=True,verbose_name='品牌',)
    model = models.CharField(max_length=30, blank=True, null=True,verbose_name='车系')
    volume = models.FloatField(blank=True, null=True,verbose_name='排量')
    gearbox = models.CharField(max_length=20, blank=True, null=True,verbose_name='变速箱')
    oldprice = models.DecimalField(verbose_name="优惠前单价", default=99, max_digits=9, decimal_places=2)
    price = models.DecimalField(verbose_name="单价", default=0, max_digits=9, decimal_places=2)
    year = models.IntegerField(blank=True, null=True,verbose_name='年份')
    age = models.IntegerField(blank=True, null=True,verbose_name='车龄')
    mileage = models.FloatField(blank=True, null=True,verbose_name='公里数')
    horsepower = models.IntegerField(blank=True, null=True,verbose_name='扭矩')
    torque = models.IntegerField(blank=True, null=True ,verbose_name='马力')
    transfer_number = models.IntegerField(blank=True, null=True,verbose_name='转手次数')
    fuel = models.FloatField(blank=True, null=True,verbose_name='汽油')
    image = models.CharField(max_length=200, blank=True, null=True,verbose_name='图片')
    creator = models.ForeignKey(UserDict, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    class Meta:
        verbose_name=verbose_name_plural="汽车"
    def __str__(self):
        return self.name


#发布的二手车记录
class GoodsRecord(models.Model):
    id = models.AutoField(primary_key=True)  # 自定义自增列
    name = models.CharField(max_length=128, verbose_name='汽车名称')
    # nums=models.IntegerField(verbose_name="库存余量",default=0)
    pic=models.ImageField(verbose_name="图片",upload_to="goodsImage",default="/defaultIocn/gooddefault.jpg")
    description = models.TextField(verbose_name='描述', default='')
    delete_flag=models.IntegerField(verbose_name="删除标识",default=0)
    #新增属性 品牌  车系  排量  变速箱   年份 车龄 公里数  扭矩  马力  转手次数  汽油  图片
    brand = models.CharField(max_length=20, blank=True, null=True,verbose_name='品牌',)
    model = models.CharField(max_length=30, blank=True, null=True,verbose_name='车系')
    volume = models.FloatField(blank=True, null=True,verbose_name='排量')
    gearbox = models.CharField(max_length=20, blank=True, null=True,verbose_name='变速箱')
    oldprice = models.DecimalField(verbose_name="优惠前单价", default=99, max_digits=9, decimal_places=2)
    price = models.DecimalField(verbose_name="单价", default=0, max_digits=9, decimal_places=2)
    year = models.IntegerField(blank=True, null=True,verbose_name='年份')
    age = models.IntegerField(blank=True, null=True,verbose_name='车龄')
    mileage = models.FloatField(blank=True, null=True,verbose_name='公里数')
    horsepower = models.IntegerField(blank=True, null=True,verbose_name='扭矩')
    torque = models.IntegerField(blank=True, null=True ,verbose_name='马力')
    transfer_number = models.IntegerField(blank=True, null=True,verbose_name='转手次数')
    fuel = models.FloatField(blank=True, null=True,verbose_name='汽油')
    image = models.CharField(max_length=200, blank=True, null=True,verbose_name='图片')
    creator = models.ForeignKey(UserDict, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    class Meta:
        verbose_name=verbose_name_plural="商品记录"
    def __str__(self):
        return self.name

#个人收藏
class ShoppingCar(models.Model):#项目
    id = models.AutoField(primary_key=True)  # 自定义自增列   
    goods=models.ForeignKey(GoodsRecord,on_delete=models.CASCADE,verbose_name="商品" )
    nums=models.IntegerField(verbose_name="购买量",default=0)   
    creator = models.ForeignKey(UserDict, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    class Meta:
        verbose_name=verbose_name_plural="购物车"
    def __str__(self):
        return self.goods.name
#个人订单主记录
class BillRecordMain(models.Model):#项目
    id = models.AutoField(primary_key=True)  # 自定义自增列
    costs=models.DecimalField(verbose_name="总金额",default="0",max_digits=9, decimal_places=2)
    nums=models.IntegerField(verbose_name="购买量",default=0)
    bill_status= models.CharField(max_length=128, verbose_name='订单状态',default="未支付")
    creator = models.ForeignKey(UserDict, on_delete=models.CASCADE, verbose_name='创建人')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    class Meta:
        verbose_name=verbose_name_plural="订单主记录"
    def __str__(self):
        return self.creator.username
#个人订单明细
class BillRecordSub(models.Model):#
    id = models.AutoField(primary_key=True)  # 自定义自增列
    main_rec = models.ForeignKey(BillRecordMain, on_delete=models.CASCADE, verbose_name="订单")
    goods = models.ForeignKey(GoodsRecord, on_delete=models.CASCADE, verbose_name="商品")
    nums = models.IntegerField(verbose_name="购买量", default=0)
    costs = models.DecimalField(verbose_name="金额", default="0", max_digits=9, decimal_places=2)
    class Meta:
        verbose_name=verbose_name_plural="订单明细"
    def __str__(self):
        return self.goods.name