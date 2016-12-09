s = str(raw_input('What is the temperature?'))
l = len(s)
t = int(s[0:l-1])

if(s[-1] == 'F'):
    print ('The converted temperature is %dC' %((t-32)*1.0/1.8))
else:
    print ('The converted temperature is %dF' %(1.8*t+32))