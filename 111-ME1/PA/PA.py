def pascal(n,data=[]):
    if data==[]:
        data=[1]
    if n==0:
        return data
    new=[]
    new.append(1)
    for i in range(0,len(data)-1):
        temp=data[i]
        temp2=data[i+1]
        new.append(temp+temp2)
    new.append(1)
    return pascal(n-1,new)
while 1:
    try:
        n=int(input())
        # n=2
        x=0
        sum=0
        result=pascal(n)
        for x in result:
            sum+=int(x)
        print(*result)
        print(sum)
    except EOFError:
        break