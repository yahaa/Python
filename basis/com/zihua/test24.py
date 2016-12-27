l = []
while True:
    s = input('Enter a number (<Enter> to quit):')
    if len(s)==0:
        break
    else:
        s = float(s)
        l.append(s)
l.sort()
ln = len(l)
if ln % 2 == 0:
    mid = (l[ln // 2] + l[ln // 2 - 1]) / 2
else:
    mid = l[ln // 2]
print('The mean is %f\nThe median is %f' % (sum(l) / ln, mid))
