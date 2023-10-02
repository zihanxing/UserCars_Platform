import numpy as np
import pandas as pd
from pandas import ExcelWriter
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

data = pd.read_excel(r'C:\Users\78531\Desktop\car_Brand.xlsx', index_col = 0)
re_data = data
mean_car_Brand = re_data['original_price'].mean()
re_data['original_price']=re_data['original_price'].fillna(mean_car_Brand )

with ExcelWriter("car_Brand .xlsx") as writer:
    re_data.to_excel(writer,sheet_name='xx')
