import numpy as np
from numpy import *
import newhypergraph as ng
import random
speedparameter=[[1,-0.39844006,0.45142351],[5,-0.001814703,-0.001814703],[11,-0.013466012,0.012015458],[13,-0.002776747,0.002402331]]
varianceparameter=[[3,45.142351],[9,51.142351],[16,5.342351],[17,66.3443],[26,15.493],[39,43.132234],[53,90.142857],[73,66.23],[81,0.778],[93,0.10097],[94,12.12329]]
codomainparameter=[[-1200,1200] for i in range(97)]
realsubgraph=[[random.randint(1,90) for i in range(random.randint(20,25))] for j in range(10)]#真正的故障超图顶点集
fakesubgraph=[[random.randint(1,90) for i in range(random.randint(20,25))] for j in range(5)]#真正的故障超图顶点集
uncertainsubgraph=[[random.randint(1,90) for i in range(random.randint(20,25))] for j in range(3)]#真正的故障超图顶点集
##线性约束参数,共18个
linearparameter=[[[6,44],[16],[0.77224]],[[6, 35],[10.66666667],[25.24142667]],[[6, 41],[5.33333333],[20.21981333]],[[40, 61],[4],[-72.7094]],[[27, 35],[1],[0.5445]],[[6, 63],[10.66666667],[22.36482667]]
,[[24, 72],[1],[0.1037]],[[29, 66],[0.5],[20.3893]],[[63, 66],[1],[-1.0361]],[[4, 40],[4],[3.27756]],[[24, 61],[1],[-0.8039]],[[29, 35],[0.5],[24.302]],[[65, 72],[2],[-44.7184]],[[24, 94, 95],[7.68990408e-04,1.00000000e+00],[-0.03458742]],
[[35, 62, 63],[0.00825038,0.00034092],[40.66194449]],[[66, 69, 72],[0.21172869,0.02703159],[35.40164024]],[[28, 61, 72],[0.0437949, 0.05082982],[40.8435434]],[[31, 46, 58, 66, 83],[3.41317414e-02,9.99457943e-01,8.31163333e-04,1.07784446e-02],[8.07059515]]
                 ]+[[[random.randint(1,90) for i in range(5)],[3.41317414e-02,9.99457943e-01,8.31163333e-04,1.07784446e-02],[8.07059515] ]for j in range(90)]
##0表示正常，1表示异常
def linear(X,Y,w,b):
    X=np.array(X)
    w=np.array(w)
    ans=np.dot(X,w)+b
    if(abs(Y-ans)<1):
        return 0
    else:
        return 1
def speed(data,index):
    if (data[speedparameter[index][0]][10]-data[speedparameter[index][0]][9] > speedparameter[index][1] and data[speedparameter[index][0]][10]-data[speedparameter[index][0]][9] < speedparameter[index][2]):
        return 0
    else:
        return 1
def variance(data,index):
    if(var([data[varianceparameter[index][0]]])<varianceparameter[index][0]):
        return 0
    else:
        return 1
def codomain(data,index):
    if(data[index] <codomainparameter[index][1] and data[index] >codomainparameter[index][0]):
        return 0
    else:
        return 1
functionparameter=[[46,83],[51,50],[61,60],[58,59],[26,25,27,28,30,31,32],[1,4],[3,33]]
def func(data,index):
    if(index==1):
        if(abs(data[46] - data[83])<0.1):
            return 0
        else:
            return 1
    if (index == 2):
        if (abs(data[51] - data[50]) < 4):
            return 0
        else:
            return 1
    if (index == 3):
        if (abs(data[61] - data[60]) < 0.64):
            return 0
        else:
            return 1
    if (index == 4):
        if (abs(data[58] - data[59]) < 0.94):
            return 0
        else:
            return 1
    if (index == 5):
        if (abs(data[26] - data[25]) < 2 and abs(data[25] - data[27]) < 5 and data[28] - data[25] and abs(data[30] - data[25]) < 1.3 and abs(data[31] - data[25]) < 6 and abs(data[32] - data[25]) < 8):
            return 0
        else:
            return 1
    if (index == 6):
        if (abs(data[1] - data[4]) < 0.1):
            return 0
        else:
            return 1
    if (index == 7):
        if (abs(data[33] - data[3]) < 0.2):
            return 0
        else:
            return 1
def detect1(data):
    connect_mat = np.array([[0 for i in range(97)]   ])##超图连通矩阵，每一行代表一个超边，每一列代表一个点，其中1表示此点在此边内，0表示不在,第一行为0号超边，没有意义
    #print(connect_mat)
    #tmp=[connect_mat]
    vweight = [1 for i in range(ng.getnumberofv(connect_mat))]  # 点权向量
    for index in range(97):##1-97号超边：值域约束
        if(codomain(data,index)):#需要更新值域约束的参数
            edge=[0 for i in range(97)]
            edge[index]=1
            #print(edge)
            connect_mat = ng.addedge(connect_mat, edge)
        else:
            edge = [0 for i in range(97)]
            connect_mat = ng.addedge(connect_mat, edge)
            vweight[index]=vweight[index]+1
    for index in range(7):##98-104号超边：函数约束
        if (func(data, index)):
            edge = [0 for i in range(97)]
            for ones in functionparameter[index]:
                edge[ones] = 1
            connect_mat = ng.addedge(connect_mat, edge)
        else:
            edge = [0 for i in range(97)]
            connect_mat = ng.addedge(connect_mat, edge)
            for ones in functionparameter[index]:
                vweight[ones] = vweight[ones] + 1/len(functionparameter[index])
    for index in range(18+80):##105-122号超边：线性约束
        length=len(linearparameter[index][0])
        if (linear([data[i] for i in linearparameter[index][0][:length-1]], data[linearparameter[index][0][length-1]],linearparameter[index][1],linearparameter[index][2][0])):
            edge = [0 for i in range(97)]
            for ones in linearparameter[index][0]:
                edge[ones] = 1
            connect_mat = ng.addedge(connect_mat, edge)
        else:
            edge = [0 for i in range(97)]
            connect_mat = ng.addedge(connect_mat, edge)
            for ones in linearparameter[index][0]:
                vweight[ones] = vweight[ones] + 1 / len(linearparameter[index][0])
    eweight = [1 for i in range(ng.getnumberofe(connect_mat))]  # 边权向量
    return vweight, eweight, np.array(connect_mat)
def detect2(data,vweight, eweight, connect_mat):
    for index in range(11):#123-133号超边：方差约束
        #print(index)
        if(variance(data,index)):
            edge=[0 for i in range(97)]
            edge[varianceparameter[index][0]]=1
            connect_mat = ng.addedge(connect_mat, edge)
        else:
            edge = [0 for i in range(97)]
            connect_mat = ng.addedge(connect_mat, edge)
            vweight[varianceparameter[index][0]]=vweight[varianceparameter[index][0]]+1
    for index in range(4):##133-136号超边：速度约束
        if (speed(data, index)):
            edge = [0 for i in range(97)]
            edge[speedparameter[index][0]]=1
            connect_mat = ng.addedge(connect_mat, edge)
        else:
            edge = [0 for i in range(97)]
            connect_mat = ng.addedge(connect_mat, edge)
            vweight[speedparameter[index][0]]=vweight[speedparameter[index][0]]+1
    #print(connect_mat.shape)
    #print(ng.getnumberofe(connect_mat))
    eweight = [1 for i in range(ng.getnumberofe(connect_mat))]  # 边权向量
    return vweight, eweight, np.array(connect_mat)
    ##方差约束、速度约束
def test():
    vweight, eweight, connect_mat=detect1([25 for i in range(97)])
    detect2([[25 for i in range(20)] for j in range(97)],vweight, eweight, connect_mat)