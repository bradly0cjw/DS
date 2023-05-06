while 1:
    try:
        n=int(input())
        max=0
        depth=1
        check=0
        back=0
        for i in range(n):
            temp=list(map(int,input().split()))
            if temp[0]==0 and temp[1]==0:
                if depth>max:
                    max=depth
                if back:
                    depth-=1
                else:
                    if check:
                        depth-=1
                        check=0
                        back=1
                    else:
                        check=1
            else:
                depth+=1
                check=0
                if back==1:
                    back=0
        if depth>max:
            max=depth
        print(max)


    except EOFError:
        break
