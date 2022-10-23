import pandas as pd
import random
from random import sample
data=pd.read_csv('text.csv')#导入csv文件
y=data.values#设置y轴数值 ,.T是转置
for t0 in range(1):
    print('time',t0,'data',y[t0])#选用t0时刻的数据
    anomalyvec=[0 for i in range(97)]
    y[t0][45]=y[t0][83]
    y[t0][51]=y[t0][50]+2
    y[t0][61]=y[t0][60]
    y[t0][58]=y[t0][59]
    y[t0][26]=y[t0][25]-1.8892
    y[t0][27]=y[t0][25]+4.585
    y[t0][28]=y[t0][25]+6.7113
    y[t0][29]=y[t0][25]+0.44
    y[t0][30]=y[t0][25]-1.2165
    y[t0][31]=y[t0][25]+5.596
    y[t0][32]=y[t0][25]+7.0226
    y[t0][3]=y[t0][33]-0.1
    funce=[[2,5],[1,2,95],[56,97,95],[56,55],[3,4,6],[34,4],[96,9],[47,84],[51,52],[61,62],[60,59],[26,27,28,29,30,31,32,33]]
    musthit=[i for i in range(97)]
    total=[]
    for i in range(0,len(funce)):
        total=total+funce[i]
    print(total)
    funceanomaly=sample(total,10)
    for fa in funceanomaly:
        y[t0][fa-1]=random.uniform(y[t0][fa-1]-399.1,y[t0][fa-1])
        anomalyvec[fa-1]=1
    musthit=list(set(musthit).difference(set(funceanomaly)))
    musthit=sample(musthit,20)
    for fa in musthit:
        y[t0][fa-1]=random.uniform(y[t0][fa-1]-1399.1,y[t0][fa-1]-1000)
        anomalyvec[fa-1]=1
    print(y[t0],anomalyvec)





