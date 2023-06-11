import math
case=int(input())
for _ in range(case):
    n=int(input())
    arr=list(map(int,input().split()))
    sum=0
    temp=[]
    for x in arr:
        status=0    
        temp.append(x)
        temp.sort()
        if (len(temp)%2)==0:
            status=-1
        else:
            status=0
        mid=int(len(temp)//2)
        # print(temp,len(temp),status,mid)    
        # print(temp[mid],temp[mid+status],math.floor((temp[mid]+temp[mid+status])/2))
        sum+=math.floor((temp[mid]+temp[mid+status])/2)
    print(sum)

