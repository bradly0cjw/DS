def hnt(n,step):
    if (n==1):
        step+=1
        return step
    else:
        step=hnt(n-1,step)
        step=hnt(n-1,step+1)
        return step
while 1:
    try:
        m=int(input())
        n=int(input())
        print(hnt(n,0)*m)
    except EOFError:
        break