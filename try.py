import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                         #导入pandas包
data = pd.read_csv("text.csv").values           	#读取csv文件
#print(data[76])
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
x = np.arange(100)
y = [0.86, 0.92, 0.8, 0.78]
y1 = [0.68, 0.64, 0.56, 0.61]
y2 = [0.57,0.65,0.66,0.76]
y3 = [0.67,0.84,0.89,0.78]

bar_width = 0.15
tick_label = [i for i in range(4)]
proges=[2*y[i]*y2[i]/(y[i]+y2[i]) for i in range(0,4)]
plt.style.use('seaborn')
plt.xlabel('time')
plt.ylabel('value')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# 设置坐标标签字体大小
cnt = 97
for i in range(97):
    tmp = data.T[i:i+1][0][50:150]
    m = np.mean(tmp)
    v = np.var(tmp)
    min = np.min(tmp)
    max = np.max(tmp)
    if(v<0.05):
        cnt = cnt - 1
        continue
    demo = (tmp - min)/(max - min)
    #demo = tmp - m
    plt.plot(x, demo, '*-', label=u"F1M,DAD")
print(cnt)
#proges1=[2*y1[i]*y3[i]/(y1[i]+y3[i]) for i in range(0,4)]
#plt.plot(x, proges1, '*-', label=u"F1M,CC")
#plt.xticks(x+bar_width/2, tick_label)
plt.show()