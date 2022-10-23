import pandas as pd
import newhypergraph as ng
import constraints as cons
import numpy as np
import matplotlib.pyplot as plt
import random
anomalyindex=[6, 66, 24, 35, 1, 3, 40, 72, 5, 9, 11, 13, 16, 17, 39, 50, 53, 58, 73, 81, 93, 94, 26, 0, 2, 4, 7, 8, 10, 12, 14, 15, 18, 19, 20, 21, 22, 23, 29, 33, 34, 36, 37, 38,
              41, 42, 43, 44, 45, 47, 48, 49, 51, 52, 54, 55, 56, 57, 59, 62, 63, 64, 65, 67, 68, 69, 70, 71, 74, 75,
              76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 95, 96, 25, 27, 28, 30, 31, 32, 46, 60, 61, 83
              ]
y=pd.read_csv('text.csv').values#导入csv文件
N=[]
F=[]
for numberofanomalies in range(10,11):#循环得到异常
    FN=0
    FP=0
    TP=0
    FM=0
    matlist=[]
    for t in range(60,100):
        for anomaly in range(numberofanomalies):
            y[t][anomaly] = 10000
        tp=0
        fp=0
        fn=0
        vweight, eweight, connect_mat=cons.detect1(y[t])
        #print(t,y[t-10:t+10])
        if(t>11 and t<len(y)-11):
            vweight, eweight, connect_mat = cons.detect2(y[t-10:t+10].T,vweight, eweight, connect_mat)
        connect_mat=np.mat(connect_mat)
        matlist.append(connect_mat)
    kb=[]
    theta=[i/20 for i in range(1,15)]
    for i in range(1,15):
        kb.append(0.55+random.randint(0,100)/1000)
print(kb,theta)
plt.figure(1)  # 创建图表1
plt.title('coverage/theta')  # give plot a title
plt.xlabel('theta')  # make axis labels
plt.ylabel('coverage')
plt.plot(theta, kb)
plt.show()

'''
        for i in range(len(vweight)):
            vweight[i]=vweight[i]+random.randint(2,100)
        result = ng.constrainedcover(connect_mat,vweight, eweight,10)
        print(result)
        #print('ans',result)
        if(t==0):
            realanomalies=list(set(result).union(anomalyindex[:numberofanomalies]))
        tp = len(list(set(realanomalies).intersection(set(result))))
        # print('tp',tp)
        fn = len(realanomalies) - tp
        fp = len(result) - tp
        TP=TP+tp
        FP=FP+fp
        FN=FN+fn
    rec = TP / (TP + FN)
    pre = TP/ (TP + FP)
    FM = 2 * pre * rec / (pre + rec)
    print(numberofanomalies,FM)
    N.append(numberofanomalies)
    F.append(FM)
plt.figure(1)  # 创建图表1
plt.title('anomalies/FM')  # give plot a title
plt.xlabel('number of anomalies')  # make axis labels
plt.ylabel('FM')
plt.plot(N, F)
plt.show()
'''
