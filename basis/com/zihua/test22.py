def f(m, y, p):
    return (m * (p / 12) * (1 + p / 12) ** (12 * y)) / ((1 + p / 12) ** (12 * y) - 1)


def getp(c, year):
    if year > 5:
        return c[4]
    elif year > 3:
        return c[3]
    elif year > 1:
        return c[2]
    else:
        return c[1]


money, year = eval(input('Enter total LOAN and YEAR separated by a comma:'))
c = input('Enter loan Mode:')
c1 = {1: 0.06, 2: 0.0615, 3: 0.064, 4: 0.0655}
c2 = {1: 0.04, 2: 0.04, 3: 0.04, 4: 0.045}
p=1
if c == 'c' or c == 'C':
    p = getp(c1, year)
else:
    p = getp(c2, year)

print('Monthly Pay:%d' %f(money*10e3,year,p))

