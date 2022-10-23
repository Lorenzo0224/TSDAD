from sklearn.linear_model import LinearRegression
import pandas as pd
from random import sample
def judge(w):
    for line in w:
        for parameter in line:
            if(parameter<0.000001):
                return 0
    return 1
y=pd.read_csv('text.csv').values#导入csv文件
all=[i for i in range(96)]
cnt=1
record=[]
data=open(r'lrc.txt','w')
data2=open(r'lrc2.txt','w')
data.truncate()
data2.truncate()
for number in range(2,40):
    for round in range(1000):
        c= sample(all, number)#随机从1-96取样
        c= sorted(c)#排序
        if(c in record):#检查是不是已经拟合过
            continue
        X = [[y[j][c[i]] for i in range(number-1)] for j in range(1000)]
        y0 = [[y[j][c[number-1]]] for j in range(1000)]
        model = LinearRegression()
        model.fit(X, y0)
        X_test = [[y[j][c[i]] for i in range(number-1)] for j in range(1001,1997)]
        y_test = [[y[j][c[number-1]]] for j in range(1001,1997)]
        w = model.coef_
        predictions = model.predict(X_test)
        #print(model.score(X_test, y_test))
        if(model.score(X_test, y_test)>0.95 and judge(w)):
            #for i, prediction in enumerate(predictions):
                #print('Predicted: %s, Target: %s' % (prediction, y_test[i]))
            print('R-squared: %.2f' % model.score(X_test, y_test),file=data)
            print("attr",c,file=data)
            print(c, file=data2)
            w = model.coef_
            b = model.intercept_ #得到bias值
            #print(len(w)) # 输出参数数目
            print(w,file=data) #输出w列表，保留5位小数
            print(b,file=data)
            #print("number",cnt)
            cnt=cnt+1
            record.append(c)
  #print('这是个测试',file=data)
data.close()
data2.close()