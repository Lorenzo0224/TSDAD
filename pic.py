import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
x = np.arange(4)
y = [0.86, 0.92, 0.8, 0.78]
y1 = [0.68, 0.64, 0.56, 0.61]
y2 = [0.57,0.65,0.66,0.76]
y3 = [0.67,0.84,0.89,0.78]

bar_width = 0.15
tick_label = ["5", "10", "15", "20"]

plt.bar(x, y, bar_width, align="center", color="blue", label="P,DAD", alpha=0.5)
plt.bar(x+bar_width, y1, bar_width, color="darkblue", align="center", label="P,CC", alpha=0.5)
plt.bar(x+bar_width*2, y2, bar_width, color="red", align="center", label="R,DAD", alpha=0.5)
plt.bar(x+bar_width*3, y3, bar_width, color="darkred", align="center", label="R,CC", alpha=0.5)
proges=[2*y[i]*y2[i]/(y[i]+y2[i]) for i in range(0,4)]

plt.xticks(fontsize=26)
plt.yticks(fontsize=26)
# 设置坐标标签字体大小
plt.plot(x, proges, 'o-', label=u"F1M,DAD")
proges1=[2*y1[i]*y3[i]/(y1[i]+y3[i]) for i in range(0,4)]
plt.plot(x, proges1, '*-', label=u"F1M,CC")
plt.xticks(x+bar_width/2, tick_label)
plt.savefig('D:\study\\research\\tsdad\ieee\IEEEtran\D3A200.png')
'''
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def main():
    plt.rcdefaults()
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题

    info_list = [(u"小给", 88, 23), (u"小人", 78, 10), (u"小民", 90, 5), (u"小一", 66, 9), (u"小个", 80, 22), (u"小胶", 48, 5), (u"小带", 77, 19)]
    positions = np.arange(len(info_list))
    names = [row[0] for row in info_list]
    scores = [row[1] for row in info_list]
    scores3 = [row[1] - 1 for row in info_list]
    proges = [row[2] for row in info_list]

    fig, ax1 = plt.subplots()

    # 成绩直方图
    ax1.bar(positions, scores, width=0.6, align='center', color='r', label=u"成绩")
    ax1.set_xticks(positions)
    ax1.set_xticklabels(names)
    ax1.set_xlabel(u"名字")
    ax1.set_ylabel(u"成绩")
    max_score = max(scores)
    ax1.set_ylim(0, int(max_score * 1.2))
    # 成绩标签
    for x,y in zip(positions, scores):
        ax1.text(x, y + max_score * 0.02, y, ha='center', va='center', fontsize=13)

    ax3 = ax1.twinx()
    ax3.bar(positions, scores3, width=0.6, align='center', color='r', label=u"成绩")
    ax3.set_xticks(positions)
    ax3.set_xticklabels(names)
    ax3.set_xlabel(u"名字")
    ax3.set_ylabel(u"成绩")
    max_score = max(scores)
    ax3.set_ylim(0, int(max_score * 1.2))
    # 成绩标签
    for x, y in zip(positions, scores):
        ax3.text(x, y + max_score * 0.02, y, ha='center', va='center', fontsize=13)

    # 变动折线图
    ax2 = ax1.twinx()
    ax2.plot(positions, proges, 'o-', label=u"进步幅度")
    max_proges = max(proges)
    # 变化率标签
    for x,y in zip(positions, proges):
        ax2.text(x, y + max_proges * 0.02, ('%.1f%%' %y), ha='center', va= 'bottom', fontsize=13)
    # 设置纵轴格式
    fmt = '%.1f%%'
    yticks = mtick.FormatStrFormatter(fmt)
    ax2.yaxis.set_major_formatter(yticks)
    ax2.set_ylim(0, int(max_proges * 1.2))
    ax2.set_ylabel(u"进步幅度")

    # 图例
    handles1, labels1 = ax1.get_legend_handles_labels()
    handles2, labels2 = ax2.get_legend_handles_labels()
    handles3, labels3 = ax3.get_legend_handles_labels()
    plt.legend(handles1+handles2+handles3, labels1+labels2+labels3, loc='upper right')

    plt.show()


if __name__ == '__main__':
    main()
'''