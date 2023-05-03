while 1:
    try:
        num=int(input())
        if num==0:
            break
        data=[]
        for i in range(num):
            data.append(list(map(float,input().split())))
        data.sort(key=lambda x:x[1])
        data.sort(key=lambda x:x[2],reverse=1)
        data.sort(key=lambda x:x[3],reverse=1)
        for i in range(len(data)):
            if i==len(data)-1:
                print(int(data[i][0]))
            else:
                print(int(data[i][0]),end=" ")
    except EOFError:
        break