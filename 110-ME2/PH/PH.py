while True:
    try:
        n,p=map(int,input().split())
        grid=list(map(int,input().split()))
        think=list(map(int,input().split()))
        all=0
        for x in think:
            all+=x
        max_grid=[]
        sublist=[]
        for y in grid:
            if y==0:
                if sublist!=[]:
                    max_grid.append(sublist)
                sublist = []
            else:
                sublist.append(y)
        if sublist:
            max_grid.append(sublist)    
        # print(max_grid)
        for xx in range(len(max_grid)):
            pass
        xx=0
        while len(max_grid)!=xx:
            # print(len(max_grid[xx]),all)
            if len(max_grid[xx])<all:
                max_grid.pop(xx)
            else:
                xx+=1
        # print(max_grid)
        # print(max_grid)
        if max_grid!=[]:
            resf=[]
            for x in range(len(max_grid)):
                grid=max_grid[x]
                res=[]
                all-=think[0]
                for i in range(len(think)):
                    max=0
                    pos=-1
                    for j in range(len(grid)-think[i]+1-all):
                        min=grid[j]
                        post=j
                        for z in range(think[i]):
                            if grid[j+z]<min:
                                min=grid[j+z]
                            post=j+z
                        # print(min,max,post)
                        if min>max:
                            max=min
                            pos=post
                        
                        # print(pos)
                    if i+1<len(think):
                        all-=think[i+1]
                    # print(pos)
                    grid=grid[pos+1:]
                    # print(*grid)
                            
                    res.append(max)
                res.sort()
                resf.append(res[0])
            resf.sort()
            print(resf[-1])
        else:
            print(0)
    except EOFError:
        break