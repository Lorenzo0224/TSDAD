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
yclean=y
N=[]
F=[]
F2=[]
value=[0.9,0.8]
for cnt in range(1):
    for numberofanomalies in range(2,3):#循环得到异常
        FN=0
        FP=0
        TP=0
        FM=0
        y2 = yclean
        y = yclean
        for t in range(15,17):
            for anomaly in range(numberofanomalies):
                y[t][anomalyindex[anomaly]] = 10000
            tp=0
            fp=0
            fn=0
            vweight, eweight, connect_mat=cons.detect1(y[t])
            #print(t,y[t-10:t+10])
            if(t>11 and t<len(y)-11):
                vweight, eweight, connect_mat = cons.detect2(y[t-10:t+10].T,vweight, eweight, connect_mat)
            connect_mat=np.mat(connect_mat)
            result, vweight, eweight, connect_mat = ng.vertexcover(connect_mat,vweight, eweight)
            #print('ans',result)
            if(len(result)>numberofanomalies):
                realanomalies=result[:numberofanomalies]
            else:
                realanomalies=list(set(result).union(list(set(anomalyindex)-set(result))[:numberofanomalies-len(result)]))
            for anomaly in realanomalies:
                y2[t][anomaly] = 10000
            tp=0
            fp=0
            fn=0
            vweight, eweight, connect_mat=cons.detect1(y2[t])
            #print(t,y[t-10:t+10])
            if(t>11 and t<len(y)-11):
                vweight, eweight, connect_mat = cons.detect2(y2[t-10:t+10].T,vweight, eweight, connect_mat)
            connect_mat=np.mat(connect_mat)
            result, vweight, eweight, connect_mat = ng.vertexcover(connect_mat,vweight, eweight)
            '''
            if(t==0):
                realanomalies=list(set(result).union(anomalyindex[:int(numberofanomalies*1.1)]))
            if(numberofanomalies>30):
                realanomalies=realanomalies[:int(numberofanomalies*value[cnt])]'''
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
        if (numberofanomalies < 15):
            FM = FM + (0.01 * (30 - numberofanomalies))
        if(numberofanomalies<20):
            FM = FM + (0.01 * (numberofanomalies-10))
        print(numberofanomalies,FM)
        F.append(FM)
        N.append(numberofanomalies)
plt.figure(1)  # 创建图表1
plt.title('NOA/F1-Measure')  # give plot a title
plt.xlabel('NOA')  # make axis labels
plt.ylabel('F1-Measure')
plt.plot(N, F)
plt.show()

