def readlrc2():
    ans=[]
    with open("lrc2.txt", "r") as f:
        for line in f.readlines():
            line = line.strip('[]\n')  #去掉列表中每一个元素的换行符
            charlist=line.split(',')
            #print([int(charlist[0])])
            numberlist=[]
            for i in range(len(charlist)):
                numberlist.append(int(charlist[i]))
            ans.append(numberlist)
    return ans
def as_num(x):
     y='{:.8f}'.format(x) # 5f表示保留5位小数点的float型
     return(y)



