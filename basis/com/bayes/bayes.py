# -*- coding: UTF-8 -*-

from numpy import *
from math import *


def loadData():
    boys = []
    girls = []
    for item in open('boy.txt', 'r').readlines():
        boys.append(map(float, list(item.split())))
    for item in open('girl.txt', 'r').readlines():
        girls.append(map(float, list(item.split())))

    return boys, girls


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


def train(boys, grils, x):
    p1 = len(boys) * 1.0 / (len(boys) + len(grils))
    bx, bq = getxq(boys)
    gx, gq = getxq(grils)
    fbx = 1.0 / sqrt(pi * 2 * bq) * exp((x - bx) ** 2 / (2 * bq))
    fgx = 1.0 / sqrt(pi * 2 * gq) * exp((x - gx) ** 2 / (2 * gq))
    return fbx * p1, fgx * (1 - p1)


def classify():
    boys, grils = loadData()
    h = float(raw_input('Input height'))
    print train(boys, grils, h)


classify()


# 最大似然估计
# 多员正态分布
# 正态分布
# 协方差
# 协方差矩阵
