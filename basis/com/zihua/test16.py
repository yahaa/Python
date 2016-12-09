s=list(raw_input())
s=map(int,s)
w=0
for i in s:
    if i==4 or i==7:
        w+=1

if w==4 or w==7:
    print 'YES'
else:
    print 'NO'
