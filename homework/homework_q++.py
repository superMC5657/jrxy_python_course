# -*- coding: utf-8 -*-
# !@time: 2021/12/31 上午7:55
# !@author: superMC @email: 18758266469@163.com
# !@fileName: homework_q++.py

#### Answer for Q++
import math

import matplotlib.pyplot as plt
import numpy as np
import talib
import tushare as ts
from matplotlib import ticker
from mplfinance.original_flavor import candlestick_ochl

tushare_token = '1c8b06446534ae510c8c68e38fc248b99f89ac3814cb55645ae2be72'
pro = ts.pro_api(tushare_token)
code = "000001.SZ"
df = pro.daily(ts_code=code)
df.drop(df.columns[0], axis=1, inplace=True)

df2 = df.query('trade_date >= "20171001"').reset_index()  # 选取2017年10月1日后的数据
df2 = df2.sort_values(by='trade_date', ascending=True)  # 原始数据按照日期降序排列
df2['dates'] = np.arange(0, len(df2))  # len(df2)指记录数
fig, ax = plt.subplots(figsize=(20, 9))
fig.subplots_adjust(bottom=0.2)  # 控制子图
###candlestick_ochl()函数的参数
# ax 绘图Axes的实例
# quotes  序列（时间，开盘价，收盘价，最高价，最低价） 时间是float类型，date必须转换为float
# width    图像中红绿矩形的宽度,代表天数
# colorup  收盘价格大于开盘价格时的颜色
# colordown   低于开盘价格时矩形的颜色
# alpha      矩形的颜色的透明度
candlestick_ochl(ax, quotes=df2[['dates', 'open', 'close', 'high', 'low']].values,
                 width=0.55, colorup='r', colordown='g', alpha=0.95)
date_tickers = df2['trade_date'].values


def format_date(x, pos):
    if (x < 0) or (x > len(date_tickers) - 1):
        return ''
    return date_tickers[int(x)]


ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  # 按一定规则选取并在水平轴上显示时间刻度
plt.xticks(rotation=30)  # 设置日期刻度旋转的角度
ax.set_ylabel('交易价格')
plt.title(code)
plt.grid(True)  # 添加网格，可有可无，只是让图像好看一些
plt.xlabel('交易日期')
plt.show()

## MACD
close = df2['close'].values
macd = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
print(macd)

##


## 计算夏普比率
df['ex_pct_close'] = df['pct_chg'] - 0.04 / 252
sharpeRatio = (df['ex_pct_close'].mean() * math.sqrt(252)) / df['ex_pct_close'].std()
print("sharpeRatio:", sharpeRatio)


## 最大回撤
def MaxDrawdown(returns):
    l = np.argmax((np.maximum.accumulate(returns) - returns) / np.maximum.accumulate(returns))
    k = np.argmax(returns[:l])
    return (returns[k] - returns[l]) / (returns[l])


maximumPullback = MaxDrawdown(close)
print("maximumPullback:", maximumPullback)


def cal_half_def(returns):
    for i in range(len(returns)):
        returns[i] = returns[0] - returns[i]
    mu = returns.mean()  # 这里使用的是均值
    temp = returns[returns < mu]
    half_deviation = (sum((temp - mu) ** 2) / len(temp)) ** 0.5
    return half_deviation

# 下行风险
half_deviation = cal_half_def(np.array(close))
print("half_deviation:", half_deviation)
