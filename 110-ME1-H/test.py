while True:
    try:
        N=int(input())
        s=[]
        if N==0:
            break
        for i in range(N):
            nums=list(map(float,input().split()))
            s.append(nums)
        s.sort(key=lambda s:float(s[-3]))
        s.sort(key=lambda s:float(s[-2]),reverse=1)
        s.sort(key=lambda s:float(s[-1]),reverse=1)
        for i in range(N):
            print(int(s[i][0]),end=" ")
    except EOFError:
        break
