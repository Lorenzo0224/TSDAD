import copy
import operator
import readlrc
import xlrd
from sklearn.linear_model import LinearRegression
import pandas as pd
from random import sample
import matplotlib.pyplot as plt
from numpy import *
from constraints import linear,speed,variance,codomain
plt.rcParams['font.sans-serif']=['SimHei']
import pandas as pd
import math
import time
import pandas as pd
import random
from random import sample
import matplotlib.pyplot as plt
def cleaning(y):
    y[t0][46] = y[t0][83]
    y[t0][51] = y[t0][50] + random.uniform(1,3)
    y[t0][61] = y[t0][60] + random.uniform(0.3,0.5)
    y[t0][58] = y[t0][59] + random.uniform(0.3,0.5)
    y[t0][26] = y[t0][25] - 1.8892
    y[t0][27] = y[t0][25] + 4.585
    y[t0][28] = y[t0][25] + 6.7113
    y[t0][29] = y[t0][25] + 0.44
    y[t0][30] = y[t0][25] - 1.2165
    y[t0][31] = y[t0][25] + 5.596
    y[t0][32] = y[t0][25] + 7.0226
    y[t0][1] = y[t0][4]
    y[t0][3] = y[t0][33] - random.uniform(0,0.1)
    return y
def insert(y):
    dice=random.randint(0, 100)#随机数决定该时间戳是否存在异常
    atr=0
    anomalyattributes=[]
    if(dice < 90):
        return atr,anomalyattributes,myvlist#有50%可能出现异常
    #anomaly=random.randint(10,59)#异常个数
    anomaly = t0%19  # 异常个数
    allattributes = [i for i in range(97)]
    anomalyattributes = sample(allattributes, anomaly)
    #print('aa',anomalyattributes)
    for i in range(len(y[t0])):
        if(i not in anomalyattributes):
            myvlist.append(vertex(i, i, y[t0][i], 1, 1, 1))  # 正常数据
        else:
            myvlist.append(vertex(i,i,y[t0][i],1,0,1))#给异常点打标签
            y[t0][i]=y[t0][i]+random.randint(10,100)
    atr=anomaly/97
    return atr,anomalyattributes,myvlist
def detect():
    for i in range(len(funce)):
        flag = 0
        for j in funce[i]:
            if (j - 1 in anomalyattributes):
                flag = 1
        if (flag == 1):
            h = hedge(i, i, [myvlist[j - 1] for j in funce[i]])
            myelist.append(h)
            #print(1)
    for i in range(len(state)):
        flag = 0
        for j in state[i]:
            if (j - 1 in anomalyattributes):
                flag = 1
        if (flag == 1):
            h = hedge(i, i, [myvlist[j - 1] for j in state[i]])
            myelist.append(h)
            #print(1)
##主函数
def anomalydetection(y):
    lre=[[random.randint(1,90) for j in range(50)]for i in range(1000)]##需要修改成正常读取线性约束
    funce=[[2,5],[1,2,95],[56,97,95],[56,55],[3,4,6],[34,4],[96,9],[47,84],[51,52],[61,62],[60,59],[26,27,28,29,30,31,32,33]]#修改成正常读取工业机理约束
    state=[[i+1] for i in range(97)]#统计量约束,需要修改成方差约束、线性约束
    myvlist=[]
    for length in range(300,301):
        funce = [[2, 5], [1, 2, 95], [56, 97, 95], [56, 55], [3, 4, 6], [34, 4], [96, 9], [47, 84], [51, 52], [61, 62],
                 [60, 59], [26, 27, 28, 29, 30, 31, 32, 33]]
        funce.extend(lre[0:length])
        numberofe=len(funce)+len(state)
        for t0 in range(0,1996):
            myvlist = []
            myelist = []
            #y=cleaning(y)#清洗数据
            atr,anomalyattributes,myvlist=insert(y)#插入异常
            if(len(anomalyattributes)==0):
                continue
            detect()
            mysubspace=subspace(1,myelist,0)
            mysubspacelist=[mysubspace]
            myhypergraph=hypergraph(1,myvlist,myelist,mysubspacelist)
            myhypergraph.partition()
            if(len(myelist)<0.5*numberofe):
                result=myhypergraph.mincover()
            else:
                result = myhypergraph.constrainedmincover()
            if (len(result) == 0):
                continue
            ans=[]
            for r in result:
                ans.append(r.index+1)
            result=ans
            print(t0,"时刻",ans,"异常")
y=pd.read_csv('text.csv').values.T#导入csv文件,y[i]代表第i列时间序列
anomalydetection(y)