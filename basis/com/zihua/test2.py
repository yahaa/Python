
def change(a):
    a.append([1,2,3])
    return a
a=[1,2,3]
print a
change(a)
print a

def fu(var1,*t):
    print var1
    for var in t:
        print var

fu(10,100)


def fc(a,b=10,c=1):
    print a,b,c

fc('ajsdf')

sum=lambda a,b:a+b;
print sum(1,3)

def tt():
    print 666

def haha():
    total=100
    print total
    return total
print haha()



