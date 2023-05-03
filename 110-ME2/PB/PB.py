while 1:
    try:
        itm,ppl=map(int,input().split(" "))
        itp=list(map(int,input().split(" ")))
        gf=list(map(int,input().split(" ")))
        sum=0
        for x in gf:
            tmp=0
            for y in itp:
                if y>=x:
                    if y<tmp or tmp==0:
                        tmp=y
            sum=sum+tmp
        print(sum)
    except EOFError:
        break