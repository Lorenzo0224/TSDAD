import numpy as np
from random import randint
import math
import time
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
checknum=0
setlist=[[randint(0,97) for i in range(randint(2,15))] for j in range(20)]#生成40个大小为2-20的集合
checklist=[]
crosslist=[]
cross_ratio = 0

def condition(selected_sets):#计算比值用于判断与miu的关系
    num_of_check = 0
    num_of_cross = 0
    for index in selected_sets:
        for e in setlist[index]:
            if(e < checknum):
                num_of_check = num_of_check + 1
            else:
                num_of_cross = num_of_cross + 1
    ratio = num_of_cross / (num_of_check + num_of_cross)
    return ratio
def condition2(set):#计算比值用于判断与miu的关系
    num_of_check = 0
    num_of_cross = 0
    for e in set:
        if(e < checknum):
            num_of_check = num_of_check + 1
        else:
            num_of_cross = num_of_cross + 1
    ratio = num_of_cross/(num_of_check+num_of_cross)
    return ratio
def gain(j, list):#计算目标函数的增长,j为一个待加入的集合编号
    selected_cross = []
    for index in list:
        for e in setlist[index]:
            if(e >= checknum):
                selected_cross = myappend(selected_cross, e)
    old_num = len(selected_cross)
    for e in setlist[j]:
        if (e >= checknum and e not in selected_cross):
            selected_cross = myappend(selected_cross, e)
    new_num = len(selected_cross)
    #print(old_num, new_num)
    return new_num - old_num
def gain2(addedset, list):#计算目标函数的增长,j为一个待加入的集合编号
    selected_cross = []
    for set in list:
        for e in set:
            if(e >= checknum):
                selected_cross = myappend(selected_cross, e)
    old_num = len(selected_cross)
    for e in addedset:
        if (e >= checknum and e not in selected_cross):
            selected_cross = myappend(selected_cross, e)
    new_num = len(selected_cross)
    #print(old_num, new_num)
    return new_num - old_num
def myappend(list,b):#将b∪在list上
    copy_of_list=[l for l in list]
    if(b not in list):
        copy_of_list.append(b)
    return copy_of_list
def dpcoverage(k,setlist,miu):##3.11 to do:将dp改为一个二维数组,selected[k][n]每一项用一个list记录已经选过的集合
    n = len(setlist)##number of elements
    dp = np.zeros((k ,n), dtype = int)#第一位代表操作步数，第二位代表最后一个决策，第三位分别存目标函数值和01串
    selected = [[[] for i in range(n)]for j in range(k)]
    for j in range(n):
        if(condition([j])>=miu):
            dp[0][j] = gain(j, [])
            #dp[0][j][1] = 1 << (j)
            selected[0][j].append(j)
    #record = np.zeros((k), dtype = int)
    for i in range(1, k):#k步
        for q in range(0, n):#当前这一步决策
            action = []
            for j in range(0, n):#上一步决策
                #print('c',int(dp[i-1][j][1]),q)
                if((q not in selected[i-1][j])#当前集合没有被选择过
                        and dp[i][q] < (dp[i-1][j] + gain(q, selected[i-1][j]))#选取增益最大的操作
                        and condition(myappend(selected[i-1][j],q))>=miu):#
                    #record[i] = record[i] + 1
                    dp[i][q] = dp[i-1][j] + gain(q, selected[i-1][j])
                    selected[i][q] = myappend(selected[i-1][j],q)
                    #print(i,q,selected[i][q])
    #print(record)
    #print(dp[0])
    #print(selected)
    max = 0
    result = 0
    for j in range(0, n):
        if(max < dp[k - 1][j]):
            max = dp[k - 1][j]
            result = selected[k - 1][j]
    return max, result
def localoptimal(k,setlist,miu):
    goodsetlist = []
    result = []
    for s in setlist:
        if(condition2(s)>=miu):
            goodsetlist.append(s)
    #if(len(goodsetlist)<k):
        #return 0, result
        #print('none')
    max = 0
    for i in range(k):
        best = 0
        choice = []
        flag = 0
        for goodset in goodsetlist:
            if(gain2(goodset, result)>best):
                best = gain2(goodset, result)
                choice = goodset
                flag = 1
        if(flag==0):
            print('not enough')
                #print(1)
        max = max + gain2(choice, result)
        result.append(choice)
    return max, result
def pic(ratio,checknum,max1list, max2list, time1list, time2list):
    saveName=str(int(ratio*10))+'_'+str(checknum)
    fig = plt.figure(figsize=(10,6))
    x = np.arange(10)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax1 = fig.add_subplot(111)
    #ax1.plot(df['yearmonth'], df['new'], )
    ax1.set_ylabel('Runtime', fontdict={'weight': 'normal', 'size': 20})
    #ax1.set_title("投资者用户数统计", fontdict={'weight': 'normal', 'size': 15})
    bar_width = 0.3
    tick_label = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    ax1.plot(x, max2list, 'o-', label=u"HCR,MVCLO", color="blueviolet")
    ax1.plot(x, max1list, '*-', label=u"HCR,DPGO", color="forestgreen")
    #ax1.bar(x, time1list, bar_width, align="center", color="green", label="P,DAD", alpha=0.5)
    #ax1.bar(x+bar_width, time2list, bar_width, color="purple", align="center", label="P,CC", alpha=0.5)
    #plt.bar(x+bar_width*2, y2, bar_width, color="red", align="center", label="R,DAD", alpha=0.5)
    #plt.bar(x+bar_width*3, y3, bar_width, color="darkred", align="center", label="R,CC", alpha=0.5)
    plt.tick_params(labelsize=23)
    labels = ax1.get_xticklabels() + ax1.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    #plt.xticks(fontsize=26)
    #plt.yticks(fontsize=26)
    ax1.set_xlabel('k', fontdict={'weight': 'normal', 'size': 20})
    ax2 = ax1.twinx()  # this is the important function
    ax2.set_ylabel('HCR',fontdict={'weight': 'normal', 'size': 20})
    #ax2.plot(x, max2list, 'o-', label=u"F1M,DAD", color="blueviolet")
    #ax2.plot(x, max1list, '*-', label=u"F1M,CC", color="forestgreen")
    font1 = {'weight': 'normal', 'size': 15}
    ax2.bar(x, time1list, bar_width, align="center", color="green", label="Runtime,DPGO", alpha=0.5)
    ax2.bar(x + bar_width, time2list, bar_width, color="purple", align="center", label="Runtime,MVCLO", alpha=0.5)
    plt.xticks(x, tick_label)
    ax2.set_xlabel('k', fontdict={'weight': 'normal', 'size': 20})
    plt.tick_params(labelsize=23)
    labels = ax2.get_xticklabels() + ax2.get_yticklabels()
    [label.set_fontname('Times New Roman') for label in labels]
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    num1 = 0.95
    num3 = 0
    num4 = 0
    num2 = 1.15
    #plt.legend(handles1 + handles2, labels1 + labels2 ,bbox_to_anchor=(num1, num2), loc = num3, prop=font1,ncol=4)
    plt.savefig('D:\study\\research\\tsdad\ieee\IEEEtran\LOGO\hc'+saveName+'.png')
    plt.clf()  # 添加上这一行，画完第一个图后，重置一下

    #ax2 = ax1.twinx()  # this is the important function
    #ax2.plot(df['yearmonth'], df['total'], 'r')

    #ax2.set_xlabel('Same')
    #参数rotation设置坐标旋转角度，参数fontdict设置字体和字体大小
    #ax1.set_xticklabels(df['yearmonth'],rotation=90,fontdict={'weight': 'normal', 'size': 15})

for checknum in range(72,93,5):
    crossnum = 97 - checknum
    checklist = [i for i in range(checknum)]
    crosslist = [i for i in range(checknum, 97)]
    cross_ratio = len(crosslist) / (len(checklist) + len(crosslist))
    ratiolist = [1, 1.1, 1.2, 1.3]
    #cross_ratio = crossnum/97
    for ratio in ratiolist:
        max1list=[]
        max2list=[]
        time1list=[]
        time2list=[]
        k=0
        for k in range(1,11):
            start = time.clock()
            max1,result1=dpcoverage(k, setlist, ratio*cross_ratio)
            end = time.clock()
            #print("The dpcovergae function run time is : %.03f seconds" % (end - start))  # 输出 ：The function run time is : 2.999 seconds
            time1 = end - start
            start = time.clock()
            max2,result2=localoptimal(k, setlist, ratio*cross_ratio)
            end = time.clock()
            #print("The greedy function run time is : %.03f seconds" % (end - start))  # 输出 ：The function run time is : 2.999 seconds
            time2 = end - start
            print(k,ratio,max1,max2,time1,time2)
            max1list.append(max1/crossnum)
            max2list.append(max2/crossnum)
            time1list.append(time1)
            time2list.append(time2*5)
        pic(ratio, crossnum, max1list, max2list, time1list, time2list)


