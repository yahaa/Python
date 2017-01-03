# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from numpy import *
import scipy.io as sio
from mpl_toolkits.mplot3d import Axes3D


def loadData():
    people = []
    cla = []
    for item in open('boy.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(1)
    for item in open('girl.txt', 'r').readlines():
        people.append(map(float, list(item.split())))
        cla.append(0)
    return array(people), cla


def classify(x, dataset, labes, k):
    datalen = dataset.shape[0]
    diffMat = tile(x, (datalen, 1)) - dataset
    sqdiffMat = diffMat ** 2
    distances = (sqdiffMat.sum(1)) ** 0.5
    distances = distances.argsort()
    boy = 0
    for i in range(k):
        boy += labes[distances[i]]
    if boy > k - boy:
        return 1
    else:
        return 0


def test(testdata, sex, k):
    dataset, lables = loadData()
    total = len(dataset)
    boy = 0
    for item in testdata:
        boy += classify(item, dataset, lables, k)
    if sex == 1:
        print '(男) 总人数为 ', total, '错误率为 ', (total - boy) * 1.0 / total
    else:
        print '(女) 总人数为 ', total, '错误率为 ', boy * 1.0 / total


def loadTest(filepath):
    people = []
    for item in open(filepath, 'r').readlines():
        people.append(map(float, list(item.split())))
    if filepath.find('boy') >= 0:
        return people, 1
    else:
        return people, 0


def draw(a, data, cla):
    ln = len(cla)
    data = data.T
    x = data[0]
    y = data[1]
    z = data[2]
    ax = plt.subplot(111, projection='3d')
    for i in range(ln):
        if cla[i]:
            ax.scatter(x[i], y[i], z[i], c='g')
        else:
            ax.scatter(x[i], y[i], z[i], c='r')
    ax.scatter(a[0], a[1], a[2], c='b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


people, sex = loadTest('girl.txt')
test(people, sex, 10)

dataset, lables = loadData()
a = [179, 64, 45]
draw(a, dataset, lables)
