# -*- coding: UTF-8 -*-
import os
import sys
import numpy as np
import operator
import matplotlib.pyplot as plt
from scipy import stats
from numpy import *
from math import *


def loadData():
    people = []
    cla = []
    for item in open('boy.txt', 'r').readlines():
        people.append(map(float, list(item.split())[0:2]))
        cla.append(1)
    for item in open('girl.txt', 'r').readlines():
        people.append(map(float, list(item.split())[0:2]))
        cla.append(0)
    return people, cla


def draw(a, w0, w1, w2, data, cla):
    x = []
    y = []
    le = sum(cla)
    for item in data:
        x.append(item[0])
        y.append(item[1])
    plt.plot(x[0:le], y[0:le], 'v', color='r')
    plt.plot(x[le:], y[le:], '^', color='g')
    plt.plot(a, f(a, w0, w1, w2), color='y')

    plt.xlim(140.0, 200.0)
    plt.ylim(30.0, 100.0)
    plt.xlabel('heiht')
    plt.ylabel('weight')
    plt.legend(('boy', 'girl'))
    plt.title('height---weight')
    plt.show()


def getMS(data, cla):
    le = sum(cla)
    boy = array(data[0:le]).T
    girl = array(data[le:]).T
    m1 = mean(boy, 1)
    s1 = cov(boy)
    m2 = mean(girl, 1)
    s2 = cov(girl)
    return m1, m2, s1, s2


def f(x, w0, w1, w2):
    return w0 / w2 - w1 / w2 * x


def classify(x, wt, w0):
    x = matrix(x)
    a = float(x * wt)
    if a > w0:
        return 1
    else:
        return 0


def loadTest(filepath):
    people = []
    for item in open(filepath, 'r').readlines():
        people.append(map(float, list(item.split())[0:2]))
    if filepath.find('boy')>=0:
        return people, 1
    else:
        return people, 0


def errorp():
    data, cla = loadData()
    M1, M2, s1, s2 = getMS(data, cla)
    sw = s1 + s2
    swi = matrix(sw).I
    wxx = swi * matrix(M1 - M2).T
    m1 = wxx.T * matrix(M1).T
    m2 = wxx.T * matrix(M2).T
    w0 = (array(m1) + array(m2)) / 2
    test, k = loadTest('boy83.txt')
    total=len(test)
    boy = 0
    for item in test:
        boy += classify(item, wxx, w0)
    if k == 1:
        print ('该测试样本为男生，总测试人数为 %d, 错误率为 %f' % (total, ((total - boy) * 1.0 / total)))
    else:
        print ('该测试样本为女生，总测试人数为 %d, 错误率为 %f' % (total, (boy * 1.0 / total)))


data, cla = loadData()
M1, M2, s1, s2 = getMS(data, cla)
sw = s1 + s2
swi = matrix(sw).I
wxx = swi * matrix(M1 - M2).T
m1 = wxx.T * matrix(M1).T
m2 = wxx.T * matrix(M2).T
w0 = (array(m1) + array(m2)) / 2
print('M1= ', M1)
print('M2= ', M2)
print('s1= ', s1)
print('s2= ', s2)
print('sw= ', sw)
print('swi= ', swi)
print('wxx= ', wxx)
print('m1= ', m1)
print('m2= ', m2)
print('w0= ', w0)

errorp()

x = np.arange(120.0, 220.0, 1)
draw(x, float(w0), float(wxx[0]), float(wxx[1]), data, cla)

