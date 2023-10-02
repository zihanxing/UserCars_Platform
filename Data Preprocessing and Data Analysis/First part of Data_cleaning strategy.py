import numpy as np
import pandas as pd
from pandas import ExcelWriter
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)

data = pd.read_excel(r'C:\Users\78531\Desktop\Total.xlsx', index_col = 0)
re_data = data
'''
    首先删除除了original_price列，所有列的NaN值。
    依据相应列以上不存在NaN的值来填补。
    '''
re_data['model'] = re_data['model'].fillna(method='ffill')
re_data['torque'] = re_data['torque'].fillna(method='ffill')
re_data['fuel'] = re_data['fuel'].fillna(method='ffill')
re_data['seller'] = re_data['seller'].fillna(method='ffill')
with ExcelWriter("Total.xlsx") as writer:
    re_data.to_excel(writer,sheet_name='xx')
