
from ShoppingApp import models
import xlrd
from AppBase.base import *

def importData(request):
    # 打开文件
    workBook = xlrd.open_workbook('F:\\shopping-site\\car.xls')
    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names()
    print(allSheetNames)
    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0]
    print(sheet1Name)
    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0)  # sheet索引从0开始
    ## 2.2 法2：按sheet名字获取sheet内容
    # sheet1_content2 = workBook.sheet_by_name('Sheet1')
    # 3. sheet的名称，行数，列数
    print(sheet1_content1.name, sheet1_content1.nrows, sheet1_content1.ncols)

    rowindex = 1
    while rowindex < sheet1_content1.nrows:
        # by_year = int(sheet1_content1.cell_value(rowindex, 1))
        try:
            brand = sheet1_content1.cell_value(rowindex, 1)
            model = sheet1_content1.cell_value(rowindex, 2)
            volume = sheet1_content1.cell_value(rowindex, 3)
            gearbox = sheet1_content1.cell_value(rowindex, 4)
            oldprice = sheet1_content1.cell_value(rowindex, 5)
            price = sheet1_content1.cell_value(rowindex, 6)
            year = int(sheet1_content1.cell_value(rowindex, 7))
            age = int(sheet1_content1.cell_value(rowindex, 8))
            mileage = sheet1_content1.cell_value(rowindex, 9)
            horsepower = int(sheet1_content1.cell_value(rowindex, 10))
            torque = sheet1_content1.cell_value(rowindex, 11)
            transfer_number = int(sheet1_content1.cell_value(rowindex, 12))
            fuel = sheet1_content1.cell_value(rowindex, 13)
            image= sheet1_content1.cell_value(rowindex, 14)
            creator = UserDict.objects.get(id=1)
            nums = 1
            name = brand + model + str(volume) + "T"


            models.GoodsRecord.objects.create(name=name, nums=nums, creator=creator, brand=brand, model=model,
                                              gearbox=gearbox, oldprice=oldprice, price=price, year=year, age=age,
                                              mileage=mileage, horsepower=horsepower, torque=torque,
                                              transfer_number=transfer_number,
                                              fuel=fuel,image=image,volume=volume
                                              )
            models.Car.objects.create(creator=creator, brand=brand, model=model,
                                              gearbox=gearbox, oldprice=oldprice, price=price, year=year, age=age,
                                              mileage=mileage, horsepower=horsepower, torque=torque,
                                              transfer_number=transfer_number,
                                              fuel=fuel, image=image, volume=volume
                                              )
        except:
            pass
        rowindex = rowindex + 1

    return successResponseCommon({}, "ok")