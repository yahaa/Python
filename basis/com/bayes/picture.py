# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
#
# plt.figure(figsize=(8,4))
# plt.plot(x,y,label="$sin(t)$",color="red",linewidth=2)
# plt.xlabel("Time(s)")
# plt.ylabel("Volt")
# plt.title("PyPlot First Example")
# plt.ylim(-1.2,1.2)
# plt.legend()
# plt.show()
def loadData():
    boy = []
    gril = []
    cla = []
    for item in open('boy.txt', 'r').readlines():
        boy.append(map(float, list(item.split())))
        cla.append(1)
    for item in open('girl.txt', 'r').readlines():
        gril.append(map(float, list(item.split())))
        cla.append(0)
    return boy, gril


def getxq(dataSet):
    x = 0
    n = len(dataSet)
    for a in dataSet:
        x += a[0]
    x /= n
    sm = 0
    for a in dataSet:
        sm += (a[0] - x) ** 2
    sm /= (n - 1)
    return x, sm


x = []
z = []
boys,grils=loadData()
bx,bq=getxq(boys)
gx,gq=getxq(grils)
for b in boys:
    x.append(b[0])
for b in grils:
    z.append(b[0])

yb = stats.norm.pdf(x, bx, bq)
yg = stats.norm.pdf(z, gx, gq)
plt.plot(x, yb, 'v',color='red')
plt.plot(z, yg, '^',color='green')
plt.show()
