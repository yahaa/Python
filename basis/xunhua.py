a=10
while a:
	print(a)
	if a==4:
		print(1000)
		print(100)
	print(10)
	a-=1
x='woshihaoren'
while x:
	print(x)
	x=x[1:]
else:
	print(123456789)

# while True:
# 	print('enter your name')
# 	y=input()
# 	if y=='ends':
# 		break
# 	print(y)
# else: 
# 	print('passt')

s=[1,2,33,4,5,6,7,8,9]
for a in s:
	print(a)
else:
	print(6666)

for x in ['jskdljf','klsdjf',87788]:print(x)
sum=0
for x in [1,3,3,4,5,6,7,8,9]:
	sum+=x
print(x)

x=[(2,3),(3,4),(5,6)]
for y in x:
	print(y)


d={'a':1999,'b':2999,'c':3999}
for b in d:
	print(d[b])


a=list(range(0,10))
print(a)

n=100
for i in range(n):
	for j in range(n):
		if i==j:print(i*i)

l1=[1,2,3,4]
l2=[5,6,7,8,9,10]
print(list(zip(l1,l2)))


for a,b in zip(l1,l2):
	print(a,b,"----",a+b)

keys=['china','japan','English']
value=[1,2,3]
d=dict(zip(keys,value))
print(d)
d['china']=10000
print(d)