# -*- coding: utf-8 -*-
# !@time: 2021/12/31 上午7:26
# !@author: superMC @email: 18758266469@163.com
# !@fileName: test.py
import numpy as np


def MaxDrawdown(return_list):
    a = np.maximum.accumulate(return_list)
    print(a)
    l = np.argmax((np.maximum.accumulate(return_list) - return_list) / np.maximum.accumulate(return_list))
    print(l)
    k = np.argmax(return_list[:l])
    print(k)
    return (return_list[k] - return_list[l]) / (return_list[l])


return_list = [100, 200, 50, 20, 300, 150, 100, 200]
mdd = MaxDrawdown(return_list)
print(mdd)
