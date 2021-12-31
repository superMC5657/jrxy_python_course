# -*- coding: utf-8 -*-
# !@time: 2021/12/31 上午7:00
# !@author: superMC @email: 18758266469@163.com
# !@fileName: homework_q4.py


#### Answer for Q4
## Q4.1
import numpy as np
import pandas as pd
import tushare as ts

tushare_token = '1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'
pro = ts.pro_api(tushare_token)
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
data = data[data['list_date'] > '20170101']
data = data[data['industry'] == '银行']
ts_code_list = data['ts_code'].values.tolist()

daily_list = []
for ts_code in ts_code_list:
    daily_list.append(pro.daily(ts_code=ts_code).dropna())

close_list = []
for daily in daily_list:
    close_list.append(daily['close'].rename(daily['ts_code'][0]))
close_df = pd.concat(close_list, axis=1)
print(close_df)



## Q4.2
pct_change_list = []
for daily in daily_list:
    pct_change = daily['pct_chg']
    pct_change.name = daily['ts_code'][0]
    pct_change_list.append(pct_change)

pct_change_df = pd.concat(pct_change_list, axis=1)

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize=(14, 10))
corrdf = pct_change_df.corr()
sns.heatmap(corrdf, cmap='RdBu', linewidths=0.05, ax=ax)

# 设置Axes的标题
ax.set_title('Correlation between stocks')
plt.show()


## Q4.3
def MaxDrawdown(returns):
    l = np.argmax((np.maximum.accumulate(returns) - returns) / np.maximum.accumulate(returns))
    k = np.argmax(returns[:l])
    return (returns[k] - returns[l]) / (returns[l])


def cal_half_def(returns):
    for i in range(len(returns)):
        returns[i] = returns[0] - returns[i]
    mu = returns.mean()  # 这里使用的是均值
    temp = returns[returns < mu]
    half_deviation = (sum((temp - mu) ** 2) / len(temp)) ** 0.5
    return half_deviation


stocks = []
for daily in daily_list:
    close_list = daily['close'].values.tolist()
    close_list.reverse()
    maximum_pullback = MaxDrawdown(close_list)
    half_deviation = cal_half_def(np.array(close_list))
    print(maximum_pullback, half_deviation)
    stocks.append((daily['ts_code'][0], maximum_pullback, half_deviation))
stocks.sort(key=lambda x: x[1])
stocks = stocks[:len(stocks) // 2]
stocks.sort(key=lambda x: x[2])
stocks = stocks[:len(stocks) // 2]
for stock in stocks:
    print(stock[0])
