n = float(input())
m = int(input())
m -= 1
l = n
while m > 0:
    n /= 4
    l += 2 * n
    m -= 1
print("%.2f\n%.2f" % (l, n / 4))
