n=int(input())
for i in range(0,n):
    k=int(input())
    name=list(map(str,input().split(" ")))
    while(len(name)!=1):
        for l in range(0,2):
            name.append(name[0])
            name.pop(0)
        name.pop(0)
    for x in name:    
        print(x)
