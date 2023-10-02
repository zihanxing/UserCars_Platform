#insert car(from excel)
import pandas as pd
from sqlalchemy import create_engine

data = pd.read_excel(r"C:\Users\lenovo\Desktop\data.xlsx", index_col = 0)  #去除index

engine = create_engine('mysql://1930026136:dsbaoganren@172.16.199.140/test?charset=utf8', encoding='utf-8')  #转UTF-8
#pandas.io.sql.to_sql(data, 'car', con=engine, schema='car', if_exists='fail' )
data.to_sql( 'car', con=engine, if_exists='append')  # 数据写入数据库