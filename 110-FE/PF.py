while 1:
    try:
        n,k=map(int,input().split())
        comp=list(map(int,input().split()))
        comp.sort()
        player=[]
        versus=[]
        sum=0
        for x in range(len(comp)):
            if x==0:
                player.append([comp[x],0,1])
            elif x==len(comp)-1:
                player.append([comp[x],1,0])
            else:
                player.append([comp[x],0,0])
        # print(*player)
        for x in range(0,len(player)):
            for y in range(x+1,len(player)):
                versus.append([x,y,(player[y][0]-player[x][0])])
        versus.sort(key=lambda x:x[2])
        # print(*versus)
        count=0
        for x in range(len(versus)):
            if count==k:
                break
            if player[(versus[x][0])][1]==1 or player[(versus[x][1])][2]==1:
                pass
            else:
                sum+=versus[x][2]
                player[(versus[x][0])][1]=1
                player[(versus[x][1])][2]=1
                count+=1
        print(sum)
    except EOFError:
        break
