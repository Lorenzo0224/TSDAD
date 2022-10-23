import operator
import time
import pandas as pd
import random
from random import sample
import matplotlib.pyplot as plt
##0表示异常，1表示正常
def speed(e):
    return 0
def variance(e):
    return 1
def codomain(e):
    return 0
def func(e):
    return 0
class vertex():
     def __init__(self,index,number,value,weight,label,ans):
         self.index=index
         self.number=number
         self.value=value
         self.weight=weight
         self.label = label
         self.ans = ans
     def addweight(self,w):#为通过检测的约束中点加权
         self.weight=self.weight+w
     def check(self):
         if(self.label==self.ans):#输出最终检测结果是否命中
             return 1
         else:
             return 0

class hedge():
    def __init__(self,index,type,vertexlist):
        self.index=index
        self.type=type
        self.vertexlist=vertexlist
    def judge(self):
       return func(self)
    def getsize(self):
        return len(self.vertexlist)
class subspace():
    def __init__(self,index,hedgelist,score):
        self.index = index
        self.hedgelist = hedgelist
        self.score=score
    def computescore(self):##为这个子空间打分，同时修改点权；增加功能：大于一定阈值直接报警，剪枝（考虑只写不做）
        sum=0
        removelist=[]
        for h in self.hedgelist:
            if(h.judge()==1):
                for v in h.vertexlist:
                    v.weight=v.weight+100000/h.getsize()
                removelist.append(h)
                print("lz")
            elif(h.judge()==0):
                sum=sum+1
        self.score=sum/len(self.hedgelist)
        self.hedgelist=list(set(self.hedgelist)^(set(removelist)))
        #print("h",self.score,len(self.hedgelist))

    def getvertexlist(self):
        ans=[]
        for e in self.hedgelist:
            for v in e.vertexlist:
                ans.append(v)
        return ans
    def mincover(self):##增加优化：用汉明距离数据库做初始化
        ans=[]
        lefte=self.hedgelist
        '''print("lefte")
        for e in lefte:
            print(e.index)
        flag=0'''
        while len(lefte)>0:
            longlist=[]
            for e in lefte:
                longlist.extend(e.vertexlist)
                '''
                if (flag == 0):
                    print("longlist")
                    for l in longlist:
                        print(l.index)
            flag=1
            '''
            x=max(set(longlist),key=longlist.count)
            removee=[]
            for e in lefte:
                if x in e.vertexlist:
                    removee.append(e)
            lefte=list(set(lefte)^(set(removee)))
            ans.append(x)
        '''print("最小覆盖")
        for v in ans:
            print(v.index)'''
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
    '''def printhypergraph(self):
        for sub in self.subspacelist:
            sub.printedge()'''
myvlist=[]
myelist=[]
ans=[i for i in range(2000)]
precision=[]
recall=[]
ratio=[]
fm=[]
klist=[]
totaltp=0
totaltn=0
totalfn=0
totalfp=0
AD=1.5
CSR=0.2
ATR=0.15
number=0
time_start=time.time()
for i in range(97):
    myvlist.append(vertex(i,i,i,1,1,1))#首先让所有点都是正常数据
#complexe=[[2,5],[1,2,95],[56,97,95],[56,55],[3,4,6],[34,4],[96,9],[47,84],[51,52],[61,62],[60,59],[26,27,28,29,30,31,32,33]]
complexe = []
cnt = 0
while(cnt<AD*67):
    size=random.randint(2,10)
    anynumber=len(complexe) % 5
    #print(anynumber)
    if(anynumber==1):
        mye = sample([i for i in range(1,12)],size)
    if (anynumber == 2):
        mye = sample([i for i in range(13, 24)], size)
    if (anynumber == 3):
        mye = sample([i for i in range(25, 39)], size)
    if (anynumber == 4):
        mye = sample([i for i in range(40, 52)], size)
    if (anynumber == 0):
        mye = sample([i for i in range(53, 67)], size)
    mye.sort()
    #print(mye)
    if(mye not in complexe):
        complexe.append(mye)
        cnt=cnt+len(mye)
singleanomaly=[i for i in range(68,97)]
total=[]
for i in range(0,len(complexe)):
    total=total+complexe[i]
total=list(set(total))
#print(total)
complexanomaly=sample(total,int(97*ATR*CSR/(1+CSR)))
singleanomaly=sample(singleanomaly,int(97*ATR/(1+CSR)))
#print(anomaly)
funce=[]
for i in range(1,97):
    if i not in singleanomaly:
        myvlist[i-1].weight=myvlist[i-1].weight+10000
    else:
        if(random.randint(1,10)<8):
            funce.append([i])
for e in complexe:
    if len(set(e).intersection(set(complexanomaly)))>0:
        funce.append(e)
    else:
        for i in e:
            myvlist[i-1].weight=myvlist[i-1].weight+10000/len(e)

#print(funce)
for i in range(len(funce)):
    h=hedge(i,i,[myvlist[j-1] for j in funce[i]])
    myelist.append(h)
mysubspace=subspace(1,myelist,0)
mysubspacelist=[mysubspace]
myhypergraph=hypergraph(1,myvlist,myelist,mysubspacelist)
myhypergraph.partition()
number=len(myhypergraph.subspacelist)
print(number)
myhypergraph.ranking(len(myhypergraph.subspacelist))
result=myhypergraph.mincover()
tp = 0
fp = 0
tn = 0
fn = 0
for v in result:
    if v.index+1 in complexanomaly:
        tp=tp+1
    elif v.index+1 in singleanomaly:
        tp=tp+1
    else: fp=fp+1
#must=int(97*ATR*(1-CSR))
#tp=tp+must*0.8
fn=len(complexanomaly)+len(singleanomaly)-tp
tn=len(myvlist)-tp-fp-fn
totaltp=totaltp + tp
totalfp = totalfp + fp
totaltn = totaltn + tn
totalfn = totalfn + fn
rec=totaltp/(totaltp+totalfn)
#print('recall',rec)
recall.append(rec)
pre = totaltp/(totaltp+totalfp)
#print('precision', pre)
precision.append(pre)
fm.append(2*pre*rec/(pre+rec))
time_end=time.time()
print('totally cost',time_end-time_start)
print('SP',pre,rec,2*pre*rec/(pre+rec))
b=pre
d=rec
f=2*pre*rec/(pre+rec)
result=set([])
for e in funce:
    result=result|set(e)
result=list(result)
tp = 0
fp = 0
tn = 0
fn = 0
for v in result:
    if v in complexanomaly:
        tp=tp+1
    elif v in singleanomaly:
        tp=tp+1
    else: fp=fp+1
#must=int(97*ATR*(1-CSR))
#tp=tp+must*0.8
fn=len(complexanomaly)+len(singleanomaly)-tp
tn=len(myvlist)-tp-fp-fn
totaltp=totaltp + tp
totalfp = totalfp + fp
totaltn = totaltn + tn
totalfn = totalfn + fn
rec=totaltp/(totaltp+totalfn)
#print('recall',rec)
recall.append(rec)
pre = totaltp/(totaltp+totalfp)
#print('precision', pre)
precision.append(pre)
fm.append(2*pre*rec/(pre+rec))
time_end=time.time()
print('totally cost',time_end-time_start)
print('BF',pre,rec,2*pre*rec/(pre+rec))
a=pre
c=rec
e=2*pre*rec/(pre+rec)
print(a,b)
print(c,d)
print(e,f)
'''
plt.figure(1)  # 创建图表1
plt.title('k/F-measure Curve')  # give plot a title
plt.xlabel('k')  # make axis labels
plt.ylabel('F-measure')
# y_true和y_scores分别是gt label和predict score
plt.figure(1)
print(klist)
plt.plot(klist, fm)
plt.show()
plt.savefig('r-f.png')
'''
'''data_arr = []

# print(data_arr)
import numpy as np
import pandas as pd
for k in range(10):
    for v in range(10):
        data_arr.append([k,v])
np_data = np.array(data_arr)

##写入文件
pd_data = pd.DataFrame(np_data)
print(pd_data)
pd_data.to_csv('pd_data.csv')'''
