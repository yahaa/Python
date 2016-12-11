s=raw_input()
s=str(int(s)+1)
while True:
    num=int(s)
    ts=list(s)
    st=set(ts)
    if len(ts)==len(st):
        print s
        break
    else:
        num+=1
        s=str(num)




