import xlrd
import matplotlib.pyplot as plt
from numpy import *
plt.rcParams['font.sans-serif']=['SimHei']
import pandas as pd

def d(x,y):
    return abs(x-y)

def readts(fname):
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name("Sheet1")
    except:
        print('no sheet in %s sheet 1', format(fname))
    nrows = sh.nrows

    total=[[] for i in range(3)]
    #print(sh.row_values(0))
    for j in range(0,1):
        arr=[]
        for i in range(0, nrows):
        #arr.append(sh.row_values(i)[0])
            if(sh.row_values(i)[j]!=""):
                total[j].append([i,sh.row_values(i)[j]])
                arr.append(sh.row_values(i)[j])
            else:
                break
    return arr[1:]


def top_k(k,V):
    sort(V)
    return (V[k-1],V[len(V)-k])


def mad(list):
    mid=median(list)
    newlist=[(list[i]-mid) for i in range(len(list))]
    return median(newlist)/len(list)


def window_judge(k,T,l):
    V=[(T[i+1]-T[i]) for i in range(len(T)-1)]
    n=len(V)
    G1_set=[]
    G2_set=[]
    for i in range(n-l-1):
        (G1,G2)=top_k(k,V[i:i+l])
        G1_set.append(G1)
        G2_set.append(G2)
    V1=mean(G1_set)
    V2=mean(G2_set)

    if(V1<V2):
        return V1-200*(V2-V1),V2+200*(V2-V1)
    else:
        return V2-200*(V1-V2),V1+200*(V1-V2)


def adscreen(T):
    y = [T[i] for i in range(len(T))]
    speed1=T[2]-T[1]
    speed2=T[len(T)-1]-T[len(T)-2]
    flag=0
    cnt=0
    start=0
    for k in range(1,len(T)):
        if(T[k]-T[k-1]<speed1 or T[k]-T[k-1]>speed2):
            if(flag==0):
                start=k
                flag=1
            cnt=cnt+1
    start=start-1
    for k in range(1,len(T)):
        if (T[k] - T[k - 1] < speed1 or T[k] - T[k - 1] > speed2):
            ans1=T[0]+k*speed1
            ans2=T[len(T)-1]-(len(T)-1-k)*speed2
            y[k]=ans1*(start+cnt-k)/cnt+ans2*(k-start)/cnt
    return y


def screen(T,G1,G2,w):
    smin=G1
    smax=G2
    y=[T[0] for i in range(len(T))]
    for k in range(1,len(T)):
        Xkmin=[]
        Xkmax=[]
        xkmin=-10000000 if(k==0) else y[k-1]+smin
        xkmax = 10000000 if (k == 0) else y[k - 1] + smax
        for i in range(k,len(T)):
            if(i<k+w):
                break
            Xkmin.append(T[i]+smin*(k-i))
            Xkmax.append(T[i]+smax*(k-i))
        xkmid=median(Xkmax+Xkmin+[T[k]])
        if(xkmax<xkmid):
            y[k]=xkmax
        elif(xkmin<xkmid):
            y[k]=xkmin
        else:
            y[k]=xkmid
    return y
def vconstraints(data,w,the):
    for k in range(len(data)-w):
        if(var(data[k:k+w])>the):
            data[k+w]=mean(data[k:k+w-1])
    return data
data=pd.read_csv('text.csv')#导入csv文件
df = pd.DataFrame()
y=data.T.values
b1=[1-(y[1][i]/y[0][i]) for i in range(1998)]
b2=[y[2][i]/(y[3][i]*9.16) for i in range(1998)]
b3=[(y[0][i]*b1[i]*3.65)/y[85][i] for i in range(1998)]
df['1']=b1
df['2']=b1
df['3']=b3
df.to_csv('949596.csv')
print(b1,b2,b3)
'''
twentyfour=[0,1,2,3,4,8,33,95,96,94,54,55,25,26,27,28,29,30,31,32,33,46,83,50,51,60,61,59,58]
one=[94]
for i in range(96):
    G1,G2=window_judge(1,y[i],10)
    if(y[i][0]<100):
        plt.plot([i for i in range(len(y[i][250:]))], y[i][250:])
plt.legend()
plt.show()
'''
        #fix=screen(y[i],G1,G2,10)
        #df[str(i)] = fix
    ##plt.plot([i for i in range(len(y[i]))],y[i],label='原始数据')
    ##plt.plot([i for i in range(len(fix))],fix,label='修复数据')
    ##plt.legend()
    ##plt.savefig(str(i)+'.png')
    ##plt.clf()
#df.set_index('1', inplace=True)
#df.to_csv('fix.csv')
''''
meishayong
ans=[i for i in range(10)]
df = pd.DataFrame()
y=data.T.values#设置y轴数值 ,.T是转置
for i  in range(25,33):
    print(y[i][0]-38.7851)
'''
'''covariance
list=[20,22,23,50,51,57,58,59,60,87,88]
for i in range(93):
    if(i in list):
        plt.plot([i for i in range(len(y[i]))], y[i], label='原始数据')
        the=var(y[i])
        fix=vconstraints(y[i],20,the)
        plt.plot([i for i in range(len(fix))], fix, label='修复数据')
        plt.legend()
        plt.savefig(str(i) + '_v.png')
        plt.clf()
        '''
''''求解速度约束
    G1,G2=window_judge(1,y[i],10)
    if(abs(G1)>0.001 or abs(G2)>0.001):
        print([i,G1, G2])
    ans.append([i,G1,G2])
    if(i==1 or i==5 or i==11 or i==13 or i==82):
        df[str(i)] = [i,G1,G2]
    fix=screen(y[i],G1,G2,10)
    plt.plot([i for i in range(len(y[i]))],y[i],label='原始数据')
    plt.plot([i for i in range(len(fix))],fix,label='修复数据')
    plt.legend()
    plt.savefig(str(i)+'.png')
    plt.clf()
df.set_index('1', inplace=True)
df.to_csv('speedconstaints.csv')
'''

