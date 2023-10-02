import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  # 确保正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 确保正常显示负号
import matplotlib.colors as mcolors

colors_lst=list(mcolors.TABLEAU_COLORS.keys()) #颜色变化

car=pd.read_excel(r'C:\Users\78531\Desktop\final.xlsx')  # 读取数据

#品牌数量 饼图 , seaborn不能画饼图，必须用plt画
plt.figure(figsize=(10,8))
df=car.groupby('brand').size()
df.name=''   # 为了消除饼图左侧显示的 None
df.plot(kind='pie',autopct='%.1f%%',fontsize=16)
plt.axis('equal')   # 为显示正圆
plt.title("Brand Proportion",fontsize=24)
plt.show()


#品牌数量 柱状图, 用sns画
plt.figure(figsize=(12,8))
# rot=0 x轴标签文字旋转角度0
sns.barplot(x=df.index,y=df.values)
plt.title("The amount of brand comparison",fontsize=24)
plt.xlabel('Brand',fontsize=20)
plt.ylabel('Amount',fontsize=20)
ax = plt.axes()		# 返回当前子图
for i,p in enumerate(ax.patches):	# 遍历图中所有条形,  ha:水平居中, va:垂直底部对齐, '%d'整数格式
    ax.text(p.get_x() + p.get_width()/2,  p.get_height()+0.2,  '%d' % df.iloc[i],
            fontsize=12, color='blue', ha='center', va='bottom') 	# 在条形上标注数字
plt.show()


#品牌的平均价格柱状图,用sns画
plt.figure(figsize=(12,8))
df=car.groupby('brand').price.mean()   # 品牌的均价
sns.barplot(x=df.index,y=df.values)
plt.title("Brand average price comparison",fontsize=24)
plt.xlabel('Brand',fontsize=20)
plt.ylabel('Average price (per ten thousand yuan)',fontsize=20)
ax = plt.axes()		# 返回当前子图
for i,p in enumerate(ax.patches):	# 遍历图中所有条形, '%.1f' 1位小数
    ax.text(p.get_x() + p.get_width()/2,  p.get_height()+0.2,  '%.1f' % df.iloc[i],
            fontsize=12, color='blue', ha='center', va='bottom') 	# 在条形上标注数字
plt.show()


#堆叠柱状图，(型号、手自动) sns不直接支持堆叠柱状图，所以还是用plt绘图
automatic=car[car.gearbox=='automatic'].groupby(['brand']).size().sort_index()  # 自动档
manual=car[car.gearbox=='manual'].groupby(['brand']).size().sort_index()  # 手动档
plt.figure(figsize=(12,8))
plt.bar(x=automatic.index,height=automatic,label='Automatic',alpha=0.8)
ax = plt.axes()		   # 返回当前子图
lst1=list(ax.patches)  # 自动档的条形
for i,p in enumerate(ax.patches):	# 遍历图中所有条形
    ax.text(p.get_x() + p.get_width()/2,  p.get_height()/2,  '%d' % automatic.iloc[i],
            fontsize=14, color='white', ha='center', va='bottom') 	# 在条形上标注数字

plt.bar(x=manual.index,height=manual,bottom=automatic,label='Manual')
lst2=list(ax.patches)  # lst2含所有条形
lst3=[p for p in lst2 if p not in lst1]   # lst3 经过筛选，只含手动档的条形
for i,p in enumerate(lst3):	# 遍历手动档条形    自动档的高度+手动档的高度
    ax.text(p.get_x() + p.get_width()/2,  lst1[i].get_height()+p.get_height(),  '%d' % manual.iloc[i],
            fontsize=14, color='blue', ha='center', va='bottom') 	# 在条形上标注数字

plt.title("Brand Automatic-Manual comparison",fontsize=24)
plt.xlabel('Brand',fontsize=20)
plt.ylabel('The amount of manual-automatic',fontsize=20)
plt.legend(fontsize=14)
plt.show()









