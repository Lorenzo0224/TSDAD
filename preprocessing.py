import pandas as pd
import random
from random import sample

from pandas import Series
import xlrd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']

def acf(TimeSeries):
    Zt = []
    LZt = []
    sum = 0
    i = 1
    while i < len(TimeSeries):
        L = TimeSeries[i::]
        LL = TimeSeries[:-i:]
        sum = sum + TimeSeries[i - 1]
        Zt.append(L)
        LZt.append(LL)
        i += 1
    sum = sum + TimeSeries[-1]
    avg = sum / len(TimeSeries)
    k = 0
    result_Deno = 0
    while k < len(TimeSeries):
        result_Deno = result_Deno + pow((TimeSeries[k] - avg), 2)
        k += 1
    print(result_Deno)

    p = 0
    q = 0
    acf = []
    while p < len(Zt):
        q = 0
        result_Mole = 0
        while q < len(Zt[p]):
            result_Mole = result_Mole + (Zt[p][q] - avg) * (LZt[p][q] - avg)
            q += 1
        acf.append(round(result_Mole / result_Deno, 3))  # 保留小数点后三位
        p += 1
    return acf


def Q(acf,n,h):
    Q=0
    for k in range(h):
        Q+=acf[k]/(n-k)
    Q*=n*(n+2)
    return Q

def planB(data):
    armean=np.mean(data)
    arstd=np.std(data)
    for k in range(len(data)):
        if(abs(data[k]-armean)>2*arstd):
            data[k]=armean
    return data


def planA(data,w):
    the=np.std(data)
    cnt=0
    for k in range(len(data)-w):
        if(np.std(data[k:k+w])>the):
            data[k+w]=np.mean(data[k:k+w-1])
            cnt=cnt+1
    return data,cnt

read=pd.read_csv('text.csv')#导入csv文件
data=read.values.T
for i in range(len(data)):
    fix,cnt=planA(data[i],15) 
    dif=list(fix-data[i])
    if(cnt<10):
        print(i)