while 1:
    try:
        n=input()
        ln=len(n)
        for i in range(1,ln+1):
            if ln%i==0:
                temp=[]
                t=""
                for j in range(ln):
                    if j%i==0 and j!=0:
                        temp.append(t)
                        t=n[j]
                    else:
                        t=t+n[j]
                temp.append(t)
                temp.sort()
                t=""
                for j in range(ln//i):
                    t=t+temp[j]
                if t!=n:
                    print(t)
                    count=1
        if count==0:
            print("orz")
    except EOFError:
        break