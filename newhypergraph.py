##包含超图的连通矩阵、顶点权重向量、超边权重向量构建、超图顶点覆盖基本算法和必要函数、超图受限顶点覆盖算法和必要函数（未完成）
import numpy as np
import random
def getnumberofv(input_mat):
    (numberofe,numberofv)=input_mat.shape
    return numberofv
def getnumberofe(input_mat):
    (numberofe,numberofv)=input_mat.shape
    return numberofe
def addedge(input_mat,edge):
    #print(getnumberofv(input_mat))
    #edgev=[(1 if(i in vlist) else 0) for i in range(getnumberofv(input_mat))]
    new_mat=np.row_stack((input_mat,edge))
    return new_mat
def addvertex(input_mat,elist):
    vertexv = [(1 if (i in elist) else 0) for i in range(getnumberofe(input_mat))]
    new_mat=np.column_stack((input_mat,vertexv))
    return new_mat
def deletevertex(input_mat,index):
    for eindex in range(getnumberofe(input_mat)):
        if(input_mat[eindex][index]==1):
            input_mat[eindex]=np.zeros(getnumberofv(input_mat))
            input_mat[eindex][index] = 0
    return input_mat
def deleteedge(input_mat,eindex):
    input_mat[eindex]=np.zeros(getnumberofv(input_mat))
    return input_mat
def vertexcover(input_mat,vweight,eweight):
    input_mat=np.array(input_mat)
    #print(len(eweight))
    ans=[]
    while(1):
        heuristic=[]
        numberofv=getnumberofv(input_mat)
        numberofe=getnumberofe(input_mat)
        for vindex in range(numberofv):
            sumweight=0
            for eindex in range(numberofe):
                if(input_mat[eindex][vindex]==1):
                    #print(len(eweight),numberofe)
                    sumweight=sumweight+eweight[eindex]
            #print(vindex,len(vweight))
            heuristic.append(sumweight/vweight[vindex])
        greedyv = heuristic.index(max(heuristic))
        ans.append(greedyv)
        input_mat=deletevertex(input_mat,greedyv)
        #print(input_mat)
        if(np.all(input_mat==0)):
            break
    return ans,vweight,eweight,input_mat
def constrainedcover(input_mat,vweight,eweight,k):
    input_mat = np.array(input_mat)
    rankedvweight=sorted(vweight)
    B=0
    for i in range(k):
        B=B+rankedvweight[i]
    while(1):
        S=[]
        numberofv = getnumberofv(input_mat)
        numberofe = getnumberofe(input_mat)
        MB=[0 for i in range(numberofv)]
        for vindex in range(numberofv):
            for eindex in range(numberofe):
                MB[vindex]=MB[vindex]+input_mat[eindex][vindex]
        rem=0.9*numberofe
        num_levels=4
        H1=[]
        H2 = []
        H3 = []
        H4 = []
        H=[H1,H2,H3,H4]
        for i in range(numberofv):
            if(vweight[i]<=B and vweight[i]>B/2):
                H1.append(i)
            elif(vweight[i]<=B/2 and vweight[i]>B/4):
                H2.append(i)
            elif (vweight[i] <= B / 4 and vweight[i] > B / 8):
                H3.append(i)
            elif (vweight[i] <= B / 8 and vweight[i] > 0):
                H4.append(i)
        K=[2,4,8,4]
        for i in range(4):
            maxindex=-1
            max=0
            for j in H[i]:
                if(vweight[j]>max):
                    maxindex=j
            if(maxindex==-1):
                break
            S.append(maxindex)
            deletevertex(input_mat,maxindex)
            rem=rem-vweight[maxindex]
            if(rem<=0): return S
            for vindex in range(numberofv):
                for eindex in range(numberofe):
                    MB[vindex] = MB[vindex] + input_mat[eindex][vindex]
                    if(MB[vindex]==0): deletevertex(input_mat,vindex)
        B=B*1.1
        if(B>sum(vweight)): return []
    # print(len(eweight))
def frequentg_m(matlist,f):
    total=matlist[0]
    for i in range(1,len(matlist)):
        total=np.sum([total,matlist[i]],axis=0)
    print(total)
    numberofv = getnumberofv(total)
    numberofe = getnumberofe(total)
    for eindex in range(numberofe):
        for vindex in range(numberofv):
            if(total[eindex][vindex]<f*len(matlist)):
                total[eindex][vindex]=0
    G=[]
    while(1):
        maximum = 0
        maxindex = -1
        for eindex in range(numberofe):
            if(max(total[eindex])>maximum):
                maxindex=eindex
                maximum=max(total[eindex])
        elist=[maxindex]
        total=deleteedge(total,maxindex)
        vlist=[]
        for vindex in range(numberofv):
            if(total[maxindex][vindex]>0):
                vlist.append(vindex)
        for v in vlist:
            for eindex in range(numberofe):
                if(total[eindex][v]>0):
                    elist.append(eindex)
                    total = deleteedge(total, eindex)
        G.append([elist])
        if (np.all(total == 0)):
            break
    return G[:int(len(G)*(1-f))+random.randint(0,6)]
def test():
    connect_mat= np.array([[0 for i in range(10)]])##超图连通矩阵，每一行代表一个超边，每一列代表一个点，其中1表示此点在此边内，0表示不在,此行表示值域约束
    for i in range(100):
        connect_mat=np.array(addedge(connect_mat,[random.randint(0,40) for _ in range(10) ]))
    vweight=[1 for i in range(getnumberofv(connect_mat))]#点权向量
    eweight=[1 for i in range(getnumberofv(connect_mat))]#边权向量
    print(connect_mat)
    ans=constrainedcover(connect_mat,vweight,eweight,20)
    print(ans)

