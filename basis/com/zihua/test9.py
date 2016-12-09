n = raw_input()
s = raw_input()
t = list(s.split(' '))
t = map(int, t)
t.sort()
t = t[::-1]
su = sum(t)
g = i = 0
for a in t:
    a = int(a)
    g += a
    su -= a
    i += 1
    if g > su:
        break
print i
