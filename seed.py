import pandas as pd
import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
def readdata(sheetnum):
    dff = pd.read_excel("D:\study\work\whb\副本根长第一次数据.xlsx", sheet_name = sheetnum, header = 0)
    #df.dropna(axis=0, how='all', inplace=True)
    df = dff.values
    print(len(df))
    drop = []
    for i in range(len(df)):
        total = 0
        for j in range(1,13):
            if(math.isnan(df[i][j])):
                total = total + 1
        if(total > 9):
            drop.append(i)
    print(sheetnum)
    print(df)
    newdf = []
    for i in range(len(df)):
        if(i not in drop):
            newdf.append(df[i])
    return newdf
def construct_vector():
    df7 = readdata("Sheet7")
    #df5 = readdata("Sheet5")
    dictionary = []
    vectors = []
    for i in range(138):
        vector = []
        for j in range(1, 6):
            vector.append(df7[i][j])
        #vector = df7[i][1 : 6]
        vectors.append(vector)
        vector[3] = vector[3] + vector[0]
        vector[4] = vector[4] + vector[1]
        dictionary.append([i, df7[i][0]])
    print(vectors)
    return vectors,dictionary
vectors, dictionary = construct_vector()
pca = PCA(n_components = 3)
newData = pca.fit_transform(vectors)
print(newData)
fig = plt.figure()
ax = plt.axes(projection='3d')
zdata = newData.T[0]
xdata = newData.T[1]
ydata = newData.T[2]
z0 = np.mean(zdata)
y0 = np.mean(ydata)
x0 = np.mean(xdata)
distance = []
for i in range(len(newData)):
    distance.append(np.linalg.norm(newData[i] - [z0, y0, x0]))
r0 = np.mean(distance)
print(r0)
ratio = []
for i in range(len(newData)):
    ratio.append([np.linalg.norm(  newData[i] - [z0, y0, x0]) /r0, i])
ratio = np.array(ratio)
ratio = ratio[ratio[:,0].argsort()]
print(ratio)
ans = []
for i in range(1,len(ratio)):
    ans.append(dictionary[int(ratio[len(ratio)-i][1])][1])
print(ans)
ans = []
for i in range(1,len(ratio)):
    ans.append(dictionary[int(ratio[len(ratio)-i][1])][1])
print(ans)
ans = []
for i in range(1,6):
    print(vectors[int(ratio[len(ratio)-i][1])])
print(ans)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
plt.show()
