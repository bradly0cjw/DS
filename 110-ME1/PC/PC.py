while True:
    try:
        n=int(input())
        if (n==0):
            break
        else:
            books=list(map(int,input().split(" ")))
            resultppl=0
            resultbooks=[]
            for i in range(0,n//2):
                resultbooks.append(books[0]+books[-1])
                books.pop(0)
                books.pop(-1)
            print(resultppl)
            for x in range(0,len(resultbooks)-1):
                print(resultbooks[x],end=" ")
            print(resultbooks[-1])    
    except EOFError:
        break
    
