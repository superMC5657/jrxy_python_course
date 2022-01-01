#### Answer for Q2
## Q2.1
import numpy as np
import pandas as pd
import tushare as ts
import random
from scipy.stats import ttest_ind, levene

# 请在 tushare.pro 网站注册并且告知学生身份，可以取得你的token

tushare_token = '1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'
pro = ts.pro_api(tushare_token)

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

data = data[data['list_date'] > '20100101']  # 过滤掉上市时间不在2010年之前的股票

ts_code_list = data.sample(n=10)['ts_code'].values.tolist()  # 随机选取10只股票

daily_list = []
for ts_code in ts_code_list:
    daily_list.append(pro.daily(ts_code=ts_code))

## Q2.2

#  获取vol序列,并以日期为索引,以股票名命名
vol_list = []
for daily in daily_list:
    daily.set_index(['trade_date'], inplace=True)
    vol = daily['vol']
    vol.name = daily['ts_code'][0]
    vol_list.append(vol)

vol_df = vol_list[0]
for i in range(1, len(vol_list)):
    vol_df = pd.merge(vol_df, vol_list[i], on="trade_date", how="inner")
print(vol_df)

## Q2.3
# (a)

# pct_change序列,同上
pct_change_list = []
for daily in daily_list:
    pct_change = daily['pct_chg']
    pct_change.name = daily['ts_code'][0]
    pct_change_list.append(pct_change)

pct_change_df = pct_change_list[0]
for i in range(1, len(pct_change_list)):
    pct_change_df = pd.merge(pct_change_df, pct_change_list[i], on="trade_date", how="inner")
print(pct_change_df)

two_ = random.sample(list(pct_change_df.columns), k=2)
pct_change_df_two = pct_change_df[two_]

# 计算两只股票的t检验
X = pct_change_df_two[two_[0]]
Y = pct_change_df_two[two_[1]]

l_xy = levene(X, Y)

if l_xy.pvalue > 0.05:
    t_xy = ttest_ind(X, Y, equal_var=True)
else:
    t_xy = ttest_ind(X, Y, equal_var=False)
print("T_statistic:", t_xy.statistic, "T_pvalue:", t_xy.pvalue)

# (b)

# 用线性回归预测下一天的股价
close_list = []
for daily in daily_list:
    series = daily['close']
    series.name = daily['ts_code'][0]
    close_list.append(series)

close_df = close_list[0]
for i in range(1, len(close_list)):
    close_df = pd.merge(close_df, close_list[i], on="trade_date", how="inner")
print(close_df)

close_df_two = close_df[two_]
X = close_df_two[two_[0]]
Y = close_df_two[two_[1]]

import statsmodels.api as sm
from statsmodels import regression


def linear_predict(series):
    def regress_y(y):
        x = np.arange(0, len(y))
        x = sm.add_constant(x)
        model = regression.linear_model.OLS(y, x).fit()
        return model

    model = regress_y(series)
    b = model.params[0]
    k = model.params[1]
    return k * (len(series) + 1) + b


X_predict = linear_predict(X)
Y_predict = linear_predict(Y)
print("X_predict:", X_predict)
print("Y_predict:", Y_predict)

## Q2.4

# 选取top10
vol_df24 = vol_df.copy()
vol_df24['mean'] = vol_df24.mean(axis=1)
vol_df24_mean_top10_index = vol_df24.loc[vol_df24['mean'].nlargest(n=10).index]
print(vol_df24_mean_top10_index)

## Q2.5
vol_df.apply(lambda x: x.fillna(x.mean()), axis=0)
vol_df.plot()
