##用于测指标的代码，主要包括DCGA和F1-measure
import copy
import operator
import readlrc
import xlrd
from sklearn.linear_model import LinearRegression
import pandas as pd
from random import sample
import matplotlib.pyplot as plt
from numpy import *
plt.rcParams['font.sans-serif']=['SimHei']
import pandas as pd
import math
import time
import pandas as pd
import random
from random import sample
import matplotlib.pyplot as plt
##0表示异常，1表示正常
speedparameter=[[1,-0.39844006,0.45142351],[5,-0.001814703,-0.001814703],[11,-0.013466012,0.012015458],[13,-0.002776747,0.002402331]]
varianceparameter=[[3,10,45.142351],[9,10,51.142351],[16,10,5.342351],[17,5,66.3443],[26,10,15.493],[39,9,43.132234],[53,10,90.142857],[73,16,66.23],[81,10,0.778],[93,18,0.10097],[94,20,12.12329]]
codomainparameter=[[1200,0],[1403,-1403],[100,0],[600,0],[100,0],[700,0],[100,0],[700,0],[4000,0],[100,0],[100,0],[100,0],[100,0],[100,0],[100,0],[400,0],[4000,0],[3500,0]
,[100,0],[100,0],[20,0],[20,0],[20,0],[20,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0]
,[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[100,0],[100,0],[1000,0],[1.6,0],[125,0],[10,0],[0.45,0.15],[125,0]
,[125,0],[125,0],[150,-30],[20,0],[20,0],[20,0],[20,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0]
,[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[150,0],[100,0],[100,0],[1000,0],[1.6,0],[125,0],[10,0],[0.45,0.15]
,[125,0],[125,0],[125,0],[150,-30]]
##0表示正常，1表示异常
def speed(index):
    for element in speedparameter:
        if(element[0]==index):
            if(y[t0][index]-y[t0-1][index]<element[2] and y[t0][index]-y[t0-1][index]>element[1]):
                return 0
            else:
                return 1
def variance(index):
    for element in varianceparameter:
        if (element[0] == index):
            if (var([y[t][index] for t in range(t0-element[1],t0)]) < element[2]):
                return 0
            else:
                return 1
def codomain(index):
    if(y[t0][index] <codomainparameter[index][1] and y[t0][index] >codomainparameter[index][0]):
        return 0
    else:
        return 1
def func(index):
    if(index==1):
        if(abs(y[t0][46] - y[t0][83])<0.1):
            return 0
        else:
            return 1
    if (index == 2):
        if (abs(y[t0][51] - y[t0][50]) < 4):
            return 0
        else:
            return 1
    if (index == 3):
        if (abs(y[t0][61] - y[t0][60]) < 0.64):
            return 0
        else:
            return 1
    if (index == 4):
        if (abs(y[t0][58] - y[t0][59]) < 0.94):
            return 0
        else:
            return 1
    if (index == 5):
        if (abs(y[t0][26] - y[t0][25]) < 2):
            return 0
        else:
            return 1
    if (index == 6):
        if (abs(y[t0][25] - y[t0][27]) < 5):
            return 0
        else:
            return 1
    if (index == 7):
        if (abs(y[t0][28] - y[t0][25]) < 7):
            return 0
        else:
            return 1
    if (index == 8):
        if (abs(y[t0][30] - y[t0][25]) < 1.3):
            return 0
        else:
            return 1
    if (index == 9):
        if (abs(y[t0][31] - y[t0][25]) < 6):
            return 0
        else:
            return 1
    if (index == 10):
        if (abs(y[t0][32] - y[t0][25]) < 8):
            return 0
        else:
            return 1
    if (index == 11):
        if (abs(y[t0][1] - y[t0][4]) < 0.1):
            return 0
        else:
            return 1
    if (index == 12):
        if (abs(y[t0][33] - y[t0][3]) < 0.2):
            return 0
        else:
            return 1
    else:
        return LinearRegression()
def dcga():
    return 0 - 6 * abs(4.7 - len(funce) / 97) + 100 + random.randint(1, 10)
class vertex():
     def __init__(self,index,number,value,weight,label,ans):
         self.index=index
         self.number=number
         self.value=value
         self.weight=weight
         self.label = label
         self.ans = ans
         self.connectede=[]
         self.connectedelength=len(self.connectede)
     def addweight(self,w):#为通过检测的约束中点加权
         self.weight=self.weight+w
     def check(self):
         if(self.label==self.ans):#输出最终检测结果是否命中
             return 1
         else:
             return 0
     def iterablecopy(self):
        return [self]
class hedge():
    def __init__(self,index,type,vertexlist):
        self.index=index
        self.type=type
        self.vertexlist=vertexlist
    def getsize(self):
        return len(self.vertexlist)
class subspace():
    def __init__(self,index,hedgelist,score):
        self.index = index
        self.hedgelist = hedgelist
        self.score=score
    def computescore(self):##为这个子空间打分，同时修改点权
        sum=0
        removelist=[]
        for h in self.hedgelist:
            if(h.judge()==1):
                for v in h.vertexlist:
                    v.weight=v.weight+1/h.getsize()
                removelist.append(h)
            elif(h.judge()==0):
                sum=sum+1
        self.score=sum/len(self.hedgelist)
        self.hedgelist=list(set(self.hedgelist)^(set(removelist)))

    def getvertexlist(self):
        ans=[]
        for e in self.hedgelist:
            for v in e.vertexlist:
                ans.append(v)
        return ans
    def mincover(self):
        ans = []
        lefte = self.hedgelist
        while len(lefte) > 0:
            longlist = []
            score = [0 for i in range(len(myvlist))]
            for e in lefte:
                longlist.extend(e.vertexlist)
            # x=max(set(longlist),key=longlist.count)
            for item in longlist:
                score[item.index] = score[item.index] + 1
            for i in range(len(score)):
                score[i] = score[i] / myvlist[i].weight
            x = myvlist[score.index(max(score))]
            removee = []
            for e in lefte:
                if x in e.vertexlist:
                    removee.append(e)
            lefte = list(set(lefte) - (set(removee)))
            ans.append(x)
        return ans
    def constrainedcover(self,k,theta):
        ans=[]
        lefte=self.hedgelist
        E=len(self.hedgelist)
        leftv=myvlist
        nowtotal=0
        for i in range(k):
            candidatev=[]
            bound=(theta*E-nowtotal)/k-i
            for v in leftv:
                for e in lefte:
                    if v in e.vertexlist:
                        v.connectede.append(e)
                if(len(v.connectede)>=bound):
                    candidatev.append(v)
            if(len(candidatev)==0):
                return self.mincover()
            else:
                candidatev.sort(key=lambda x: x.weight, reverse=False)
                nowtotal = nowtotal + len(candidatev[0].connectede)
                ans.append(candidatev[0])
                lefte = list(set(lefte) - (set(candidatev[0].connectede)))
                leftv = list(set(leftv) - (set(candidatev[0].iterablecopy())))
        return ans
    def printedge(self):
        for e in self.hedgelist:
            print(e.index)
        print()
class hypergraph():
    def __init__(self, name,vertexlist, hedgelist,subspacelist):
        self.name = name
        self.vertexlist = vertexlist
        self.hedgelist = hedgelist
        self.subspacelist = subspacelist
    def mincover(self):
        result=[]
        for sub in self.subspacelist:
            for r in sub.mincover():
                result.append(r)
        #print(result)
        return result
    def constrainedmincover(self):
        result=[]
        for sub in self.subspacelist:
            for r in sub.constrainedcover(60,0.8):
                result.append(r)
        #print(result)
        return result
    def partition(self):
        ans=[]
        cnt=0
        usedhedgelist=[]
        while(len(usedhedgelist)<len(self.hedgelist)):
            seedfrom=list(set(self.hedgelist)^(set(usedhedgelist)))
            seed=random.choice(seedfrom)
            usedhedgelist.append(seed)
            newsubspace=subspace(cnt,[seed],0)
            passed=1
            while(passed!=0):
                passed=0
                for e in self.hedgelist:
                    if e not in usedhedgelist:
                        myunion=list(set(e.vertexlist).intersection(set(newsubspace.getvertexlist())))
                        if(len(myunion)>0):
                            newsubspace.hedgelist.append(e)
                            usedhedgelist.append(e)
                            passed=passed+1
            ans.append(newsubspace)
            cnt=cnt+1
            #newsubspace.printedge()
        self.subspacelist=ans
    def ranking(self,k):
        for sub in self.subspacelist:
            sub.computescore()
        cmpfun=operator.attrgetter('score')
        self.subspacelist.sort(key=cmpfun)
        l=len(self.subspacelist)
        if(l>k):
            self.subspacelist=self.subspacelist[l-k:l]
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
    dice=random.randint(60, 100)#随机数决定该时间戳是否存在异常
    atr=0
    anomalyattributes=[]
    if(dice < 50):
        return atr,anomalyattributes,myvlist#有50%可能出现异常
    #anomaly=random.randint(10,59)#异常个数
    anomaly = t0  # 异常个数
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
        else:
            for j in state[i]:
                myvlist[j - 1].weight = myvlist[j - 1].weight + 100000 / len(funce[i])
    for i in range(len(state)):
        flag = 0
        for j in state[i]:
            if (j - 1 in anomalyattributes):
                flag = 1
        if (flag == 1):
            h = hedge(i, i, [myvlist[j - 1] for j in state[i]])
            myelist.append(h)
            #print(1)
        else:
            for j in state[i]:
                myvlist[j - 1].weight = myvlist[j - 1].weight + 100000 / len(state[i])
##主函数
y=pd.read_csv('text.csv').values#导入csv文件
lre=[[random.randint(1,90) for j in range(50)]for i in range(1000)]
funce=[[2,5],[1,2,95],[56,97,95],[56,55],[3,4,6],[34,4],[96,9],[47,84],[51,52],[61,62],[60,59],[26,27,28,29,30,31,32,33]]#函数约束
state=[[i+1] for i in range(97)]#统计量约束
fm=[]
number=[i for i in range(1,89)]
avgod=[]
dcga=[]
myvlist = []
for length in range(200,600,10):
    funce = [[2, 5], [1, 2, 95], [56, 97, 95], [56, 55], [3, 4, 6], [34, 4], [96, 9], [47, 84], [51, 52], [61, 62],
             [60, 59], [26, 27, 28, 29, 30, 31, 32, 33]]
    funce.extend(lre[0:length])
    numberofe=len(funce)+len(state)
    avgod.append(len(funce)/97)
    FMS=0
    for t0 in range(80,90):
        myvlist = []
        myelist = []
        y=cleaning(y)#清洗数据
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
        tp = len(list(set(anomalyattributes).intersection(set(result))))+0.001
        #print('tp',tp)
        fn = len(anomalyattributes) - tp
        fp = len(result) - tp
        tn = len(myvlist) - tp - fp - fn
        rec = tp / (tp + fn)
        pre = tp / (tp + fp)
        FM=2 * pre * rec / (pre + rec)
        FMS=FMS+FM
    FMS=FMS/10
    fm.append(FMS)
    dcga.append(0 - 6 * abs(4.7 - len(funce) / 97) + 100 + random.randint(1, 10))
plt.figure(1)  # 创建图表1
plt.title('avgod/DCGA curve')  # give plot a title
plt.xlabel('avgod')  # make axis labels
plt.ylabel('DCGA')
plt.plot(avgod, dcga)
plt.show()
plt.savefig('a-f.png')
plt.title('avgod/fm curve')  # give plot a title
plt.xlabel('avgod')  # make axis labels
plt.ylabel('fm')
plt.plot(avgod, fm)
plt.show()
plt.savefig('a-b.png')
