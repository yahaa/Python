luckies = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
s = raw_input()
t = int(s)
ans = False
s = s.replace('4', '')
s = s.replace('7', '')
if len(s) <= 0:
    ans = True
if ans:
    print 'YES'
else:
    s = t
    for a in luckies:
        if s % a == 0:
            ans = True
    if ans:
        print 'YES'
    else:
        print 'NO'




