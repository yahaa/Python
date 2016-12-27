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


def draw(data, cla):
    x = []
    y = []
    le = sum(cla)
    for item in data:
        x.append(item[0])
        y.append(item[1])
    plt.plot(x[0:le], y[0:le], 'v', color='r')
    plt.plot(x[le:], y[le:], '^', color='g')

    plt.xlim(120.0, 220.0)
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


data, cla = loadData()
M1, M2, s1, s2 = getMS(data, cla)
sw = s1 + s2
swi = matrix(sw).I
wxx = swi * matrix(M1 - M2).T
m1=wxx.T*matrix(M1).T
m2=wxx.T*matrix(M2).T
w0=(array(m1)+array(m2))/2
print('M1= ', M1)
print('M2= ', M2)
print('s1= ', s1)
print('s2= ', s2)
print('sw= ', sw)
print('swi= ', swi)
print('wxx= ', wxx)
print('m1= ', m1)
print('m2= ', m2)
print('w0= ',w0)
