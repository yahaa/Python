# -*- coding: UTF-8 -*-
from scipy import stats


def loadData():
    people = []
    cla = []
    for item in open('boy.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(1)
    for item in open('girl.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(0)
    return people, cla


def getxq(dataSet):
    x = 0
    n = len(dataSet)
    for a in dataSet:
        x += a[0]
    x /= n
    sum = 0
    for a in dataSet:
        sum += (a[0] - x) ** 2
    sum /= n
    return x, sum


def train1(dataSet, cla):
    p1 = sum(cla) * 1.0 / len(dataSet)
    tob = sum(cla)
    bx, bq = getxq(dataSet[0:tob])
    gx, gq = getxq(dataSet[tob:])
    return bx, bq, gx, gq


def classify(h):
    p1 = 0.5
    people, cla = loadData()
    bx, bq, gx, gq = train1(people, cla)
    pab = stats.norm.pdf(h, bx, bq)
    pag = stats.norm.pdf(h, gx, gq)
    px = pab * p1 + pag * (1 - p1)
    return pab * p1 / px, pag * (1 - p1) / px


p1, p2 = classify(180)
print ('是男生的概率为：%f' % p1)
print ('是女生的概率为：%f' % p2)











# 最大似然估计
# 多员正态分布
# 正态分布
# 协方差
# 协方差矩阵
