while True:
    try:
        t1="16 3"
        t2="1 0 0 2 0 0 3 0 0 4 5 6 0 0 1"
        t3="1 1 3"
        n,p=map(int,t1.split())
        grid=list(map(int,t2.split()))
        think=list(map(int,t3.split()))
        n,p=map(int,input().split())
        grid=list(map(int,input().split()))
        think=list(map(int,input().split()))
        all=0
        for x in think:
            all+=x
        res=[]
        all-=think[0]
        for i in range(len(think)):
            max=0
            pos=-1
            new=[]
            req=grid[-(think[i]+all):]
            new=grid[len(grid)-think[i]+1-all-req.count(0)-1:]
            while req.count(0)!=new.count(0):
                req=grid[-(think[i]+all+new.count(0)+1):]
                new=grid[len(grid)-think[i]+1-all-req.count(0)-1:]
                print(req,new,req.count(0),new.count(0))

            for j in range(len(grid)-think[i]+1-all-req.count(0)):
                current=[]
                min=0
                for z in range(think[i]):
                    current.append(grid[j+z])
                current.sort()
                if current[0]!=0:
                    min=current[0]
                post=j+z
                if min>max:
                    max=min
                    pos=post
                print(len(grid)-think[i]+1-all-req.count(0),len(grid),think[i]-1,all,req.count(0))
                print(min,max,post,grid[j],current,grid)
                print(pos)
            if i+1<len(think):
                all-=think[i+1]
            # print(pos)
            grid=grid[pos+1:]
            # print(*grid)      
            res.append(max)
            # print(res)
        res.sort()
        print(res[0])
        # break
    except EOFError:
        break