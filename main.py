#利用字典设置层次结构中两层之间的约束条件

import pandas as pd
import numpy as np
import math as mt
from scipy import stats

# 列表形式
f43 = {"Tom": [[1, 2, 3], 11], "Jerry": [[4, 5], 12], "Mike": [[6, 7], 13], "Green": [[8, 9, 10], 14]}
f32 = {"Jack": [[11, 12], 15], "Kim": [[13, 14], 16]}
print(f43["Green"][1])

# 元组形式
f43_t = {"Tom": ((1, 2, 3), 11), "Jerry": ((4, 5), 12), "Mike": ((6, 7), 13), "Green": ((8, 9, 10), 14)}
f32_t = {"Jack": ((11, 12), 15), "Kim": ((13, 14), 16)}
f21_t = {"James": ((15, 16), 17)}

print(f43_t["Mike"][0])
print(f32_t["Jack"][1])
print(f21_t["James"][1])

vFcrt = (f43_t, f32_t, f21_t)
print(vFcrt[1])

# 元组内只有一个元素时要加逗号
vLabelcrt = (("Tom", "Jerry", "Mike", "Green"), ("Jack", "Kim"), ("James",))
print(vLabelcrt[1])


# 统计层次结构约束条件中的元素
def GetCrtTotal(vFcrt):
    iSum = 0
    iLen = len(vFcrt)
    i = 0
    while i < iLen:
        for vVal in vFcrt[i].values():
            iLen2 = len(vVal[0])
            iSum += iLen2
        i += 1
    return iSum


iSum = GetCrtTotal(vFcrt)
print(iSum)


# 检测层次结构条件和标签是否一致
def CheckCrtConsistent(vFcrt, vLabelcrt):
    iLen1 = len(vFcrt)
    iLen2 = len(vLabelcrt)
    if iLen1 != iLen2:
        print(iLen1)
        return False

    i = 0
    while i < iLen1:
        iLen3 = len(vFcrt[i])
        iLen4 = len(vLabelcrt[i])
        if iLen3 != iLen4:
            print(iLen3, iLen4, i)
            return False
        j = 0
        for szKey in vFcrt[i].keys():
            szLabel = vLabelcrt[i][j]
            if szKey != szLabel:
                print(szKey)
                return False
            j += 1
        i += 1
    return True


print(CheckCrtConsistent(vFcrt, vLabelcrt))

# list元素求和
a = [1, 2, 3]
print(sum(a))
