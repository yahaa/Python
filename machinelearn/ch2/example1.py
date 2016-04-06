import math
def format_name(s):
	return s[0].upper()+s[1:].lower()
s=['tons','butr','tjru']
print (map(format_name,s))

def prod(x,y):
	return x*y
s=[1,2,3,4,5,6,7,8,9]
print reduce(prod, s)
y=100
print (math.sqrt(y)*math.sqrt(y))

def cmp_ignore_case(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1<s2 :return -1
    if s1>s2 :return 1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)