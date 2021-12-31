#### Answer for Q1
## Q1.1
import numpy as np
from random import randint
import pandas as pd

A = np.zeros([10, 4])
for x in range(A.shape[0]):
    for y in range(A.shape[1]):
        A[x, y] = randint(0, 100)
print(A)

B = np.random.normal(size=[40])
print(B)

## Q1.2
B = np.resize(B, new_shape=[4, 10])
C = np.matmul(A, B)
print(C)

C_I = np.linalg.inv(C)
print(C_I)

C_det = np.linalg.det(C)
print(C_det)

## Q1.3
# (a)
C_mean = np.mean(C)
a_list = []
for x in range(C.shape[0]):
    for y in range(C.shape[1]):
        if C[x, y] > C_mean:
            a_list.append(C[x, y])
print(a_list)
# (b)
b_list = []
for x in range(C.shape[0]):
    for y in range(C.shape[1]):
        if C[x, y] > C_mean:
            b_list.append((x, y))
print(b_list)

## Q1.4
df = pd.DataFrame(C)
df.columns = list('ABCDEFGHIJ')
print(df)

## Q1.5
df.to_csv("C:\\rand_num.csv")

