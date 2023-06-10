case=1
while 1:
    try:
        k,l=map(int,input().split())
        if k==-1 and l==-1:
            break
        terms=1
        tempk=k
        while 1:
            if tempk==1:
                break
            else:
                if tempk%2!=1:
                    tempk=int(tempk/2)
                else:
                    tempk=3*tempk+1
                    if tempk>l:
                        break
                terms+=1
        print("Case %d: K = %d, limit = %d, number of terms = %d"%(case,k,l,terms))
        case+=1
    except EOFError:
        break