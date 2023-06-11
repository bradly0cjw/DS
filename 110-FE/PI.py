while 1:
    try:
        l,u=map(int,input().split())
        bomb=int(input())
        result=0
        if bomb<l or bomb>u:
            result=-1
        else:
            while 1:
                mid=int((l+u)/2)
                result+=1
                if mid==bomb:
                    break
                elif bomb>mid:
                    l=mid+1
                else:
                    u=mid-1
        print(result)
    except EOFError:
        break