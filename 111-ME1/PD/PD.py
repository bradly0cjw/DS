while 1:
    try:
        n,ppl=input().split()
        day,month=map(int,n.split("/"))
        ppl=int(ppl)
        absent=list(map(int,input().split()))
        att=[]
        std=[]
        last=0
        repeat=day
        add=day%10
        current=day
        status=-1
        jjz=0

        while len(att)<8:
            if current>ppl:
                if add==0:
                    current=10
                else:
                    current=add
            while current in std:
                if current>ppl:
                    if add==0:
                        current=10
                    else:
                        current=add
                current=last+1
                add=(add+1)%10
            if current in absent:
                jjz+=1
            else:
                att.append(current)
            std.append(current)
            last=current
            current+=10

        print(*att)
        print("Li's angry number is %d"%jjz)    
    except EOFError:
        break