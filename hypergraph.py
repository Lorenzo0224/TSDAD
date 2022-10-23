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
from constraints import linear,speed,variance,codomain
plt.rcParams['font.sans-serif']=['SimHei']
import pandas as pd
import math
import time
import pandas as pd
import random
from random import sample
import matplotlib.pyplot as plt
##0表示异常，1表示正常
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

    def dcga(self,thevlist):
        sum=0
        lefte=self.hedgelist
        removee=[]
        for i in range(len(thevlist)):
            for e in lefte:
                if(thevlist[i] in e.vertexlist):
                    thevlist[i].connectede.append(e)
                    removee.append(e)
            lefte = list(set(lefte) - (set(removee)))
            sum=sum+len(thevlist[i].connectede)/(thevlist[i].weight* math.log(i, 2))
        #print(sum)

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

