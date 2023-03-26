def S(times,data=None):
    if data==None:
        data=[1]
    if times==0:
        return data
    count=1
    new=[]
    for i in range(len(data)-1):
        if data[i]==data[i+1]:
            count=count+1
        else:
            new.append(count)
            new.append(data[i])
            count=1
    new.append(count)
    new.append(data[-1])
    return S(times-1,new)

while 1:
    try:
        n=int(input())
        if n==-1:
            break
        temp=S(n)
        for x in range(len(temp)-1):
            print(temp[x],end="")
        print(temp[-1])
            
    except EOFError:
        break
