import math


def f(a):
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return 0
    return 1


s = input()
a = int(s)
b = int(s[::-1])
if f(a) == 1 and f(b) == 1:
    print('yes')
else:
    print('no')
