n = int(raw_input())
ans = 0
while n > 0:
    s = raw_input()
    s = list(s.split(' '))
    s = map(int, s)
    if s[1]-s[0] >= 2:
        ans += 1
    n -= 1
print ans
