y='you are you'
def func(y):
	y='ninini'
print(y)

def change(a,b):
	a=100
	b[0]=1000
	return a,b
a=1234
b=[1,22,3,4]
t,y=change(a, b)
print(a)
for x in b:
	print(x)
print(t,y)

def fu(a=100,b=100,c=100):
	print(a,b,c)

fu(100,1999,100)

def mysum(l):
	if not l:
		return 0
	else:
		return l+mysum(l-1)
print(mysum(10))

def sum2(L):
	if not L:
		return 0
	else:
		print(L)
		return L[0]+sum2(L[1:])
L=[1,2,3,4,5,6,7,8,9,10]
sum2(L)


def sum3(L):
	return 0 if not L else L[0]+sum3(L[1:])
print('xxxxxxxxxxxxxxx')
print(sum3(L))

def sum4(L):
	if not L:
		return 0
	return sum4(L[1:])
print(sum4(L))
sum=0
while L:
	sum+=L[0]
	L=L[1:]
print(sum)
print(L)
L=[1,2,3,4,5,6,7,8,9,10]
sum=0
for x in L:
	sum+=x
print(sum)
L=[1,2,3,4,[5,[6,[7,8,9],10]],11,12,13]
def sumtree(L):
	total=0
	for x in L:
		if not isinstance(x, list):
			total+=x
		else:
			total+=sumtree(x)
	return total
print(sumtree(L))
x=sumtree
v=[1,2,3,4,5,6,7,8,9,10]
print(x(v))
print(sumtree.__name__)
print(dir(sumtree))
print(sumtree.func_code)
print(sumtree.)



