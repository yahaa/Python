s = raw_input().split(' ')
s = map(int, s)

def fun(n):
    sums = 0
    for i in range(1, n+1):
        sums += i
    return sums
t = s[1]-s[0]*fun(s[2])
if t >= 0:
    print 0
else:
    print -t



