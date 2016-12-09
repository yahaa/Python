mu = list()
for i in range(5):
    s = raw_input()
    s = list(s.split(' '))
    mu.append(s)
for i in range(1,6):
    flag = False
    for j in range(1,6):
        if mu[i-1][j-1] == '1':
            flag = True
            break
    if flag:
        break
print abs(i-3)+abs(j-3)+1



