# -*- coding: UTF-8 -*-
from scipy import stats
from numpy import *
from math import *


def loadData():
    people = []
    cla = []
    for item in open('boy.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(1)
    for item in open('girl.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(0)
    print people
    return people, cla


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


def train1(dataSet, cla):
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
    pb = pab * p1 / px
    pg = pag * (1 - p1) / px
    if pb > pg:
        return 1
    else:
        return 0


def getXQ2(dataSet):
    dataSet = array(dataSet).T
    u = mean(dataSet, 1)
    q = cov(dataSet)
    return u, q


def train2(dataSet, cla):
    tob = sum(cla)
    bx, bqm = getXQ2(dataSet[0:tob])
    gx, gqm = getXQ2(dataSet[tob:])
    return bx, bqm, gx, gqm


def classify2(p):
    p1 = 0.5
    data, cla = loadData()
    bx, bqm, gx, gqm = train2(data, cla)
    pab = nnorm(p, bx, bqm)
    pag = nnorm(p, gx, gqm)
    px = pab * p1 + pag * (1 - p1)

    pb = pab * p1 / px
    pg = pag * (1 - p1) / px
    if pb > pg:
        return 1, pb, pg
    else:
        return 0, pb, pg


def nnorm(p, u, qm):
    a = array(p - u)
    d = float(len(p))
    return exp(-0.5 * dot(dot(a.T, linalg.inv(qm)), a)) / ((2 * pi) ** (d / 2) * (linalg.det(qm)) ** 0.5)


def loadTest(fileName):
    test = []
    for item in open(fileName, 'r').readlines():
        test.append(map(float, list(item.split())))

    if str(fileName).find('boy') >= 0:
        return test, 1
    else:
        return test, 0


def errorp2(test, k):
    total = len(test)
    boy = 0
    for p in test:
        boy += classify2(p)[0]
    if k == 1:
        print ('该测试样本为男生，总测试人数为 %d, 错误率为 %f' % (total, ((total - boy) * 1.0 / total)))
    else:
        print ('该测试样本为女生，总测试人数为 %d, 错误率为 %f' % (total, (boy * 1.0 / total)))


def errorp1(test, k):
    total = len(test)
    boy = 0
    for p in test:
        boy += classify(p[0])
    if k == 1:
        print ('该测试样本为男生，总测试人数为 %d, 错误率为 %f' % (total, ((total - boy) * 1.0 / total)))
    else:
        print ('该测试样本为女生，总测试人数为 %d, 错误率为 %f' % (total, (boy * 1.0 / total)))


def addS(p):
    s = [[0, 10], [15, 0]]
    kind, p1, p2 = classify2(p)
    pp = [p1, p2]
    sm = zeros(2)
    for k in range(len(s)):
        for i in s[k]:
            sm[k] += s[k][i] * pp[i]
    print sm


def parzen(x, dataSet):
    p = 0.0
    for item in dataSet:
        p += f(x - item[0])
    return p


def f(x):
    return exp(-0.5 * x ** 2) / ((2 * pi) ** 0.5)


def classify3(x):
    p1 = 0.5
    peoples, cla = loadData()
    n = sum(cla)
    pmb = parzen(x, peoples[0:n])
    pmg = parzen(x, peoples[n:])

    px = pmb * p1 + pmg * (1 - p1)
    pb = pmb * p1 / px
    pg = pmg * (1 - p1) / px
    if pb > pg:
        return 1, pb, pg
    else:
        return 0, pb, pg


def errorp3(test, k):
    total = len(test)
    boy = 0
    for p in test:
        boy += classify3(p[0])[0]
    if k == 1:
        print ('该测试样本为男生，总测试人数为 %d, 错误率为 %f' % (total, ((total - boy) * 1.0 / total)))
    else:
        print ('该测试样本为女生，总测试人数为 %d, 错误率为 %f' % (total, (boy * 1.0 / total)))


test, k = loadTest('boy.txt')
errorp2(test, k)
