while 1:
    try:
        n=input()
        ans=[]
        for x in range(len(n)):
            temp=n[x:]+n[:x]
            if temp not in ans:
                ans.append(temp)
        print(*ans)        
    except EOFError:
        break