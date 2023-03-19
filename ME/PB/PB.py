while True:
    try:
        m=list(map(int,input().split(" ")))
        n=list(map(int,input().split(" ")))
        # m=[1,3,5,7,9]
        # n=[3,2,3,2]
        stack=[]
        old=m
        new=[]
        for i in range(1,n[0]+1):
            while((len(old)//n[i])>=1):
                for k in range(0,n[i]):
                    stack.append(old[0])
                    old.pop(0)
                for j in range(0,n[i]):    
                    new.append(stack[-1])
                    stack.pop()
            for l in range(0,len(old)):
                new.append(old[l])
            old=new
            new=[]
            # 注意Python 為pass by reference 
            # 若直接old=new
            # 不可直接new.clear()
            # 須以賦值方式將new的每項單獨傳入old
            # 才可 new.clear()
        for x in range(0,(len(old)-1)):
            print(old[x],end=" ")
        print(old[-1])
    except EOFError:
        break