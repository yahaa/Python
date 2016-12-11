
ln=int(raw_input())
s=raw_input().split(' ')
s=map(int,s)
a=list(s)
for i in range(ln):
    a[s[i]-1]=i+1

def fun(lit):
    ts=''
    for t in lit:
       ts+=str(t)+' '
    return ts

print fun(a)


