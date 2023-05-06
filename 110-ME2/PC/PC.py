def ins(srt,rnd):
    inp=[]
    inp=inp+srt
    print("1")
    for i in range(rnd):
        for j in range(i,0,-1):
            if inp[j]>inp[j-1]:
                inp[j],inp[j-1]=inp[j-1],inp[j]
            else:
                break
        print(*inp)
def bbs(srt,rnd):
    inp=[]
    inp=inp+srt
    print("2")
    for j in range(rnd):
        for i in range(len(inp)-1,0,-1):
            if inp[i]>inp[i-1]:
                inp[i],inp[i-1]=inp[i-1],inp[i]
        print(*inp)
def sls(srt,rnd):
    inp=[]
    inp=inp+srt
    print("3")
    for j in range(rnd):
        max=inp[j]
        key=j
        for i in range(len(inp)-1,j-1,-1):
            if inp[i]>max:
                max=inp[i]
                key=i
        inp[j],inp[key]=inp[key],inp[j]        
        print(*inp)




while 1:
    try:
        depart,rnd=map(int,input().split())
        case=list(map(int,input().split()))
        ins(case,rnd)
        bbs(case,rnd)
        sls(case,rnd)
    except EOFError:
        break