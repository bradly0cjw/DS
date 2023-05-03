while 1:
    try:
        n=int(input())
        calc=0
        if n==0:
            break
        while 1:
            # print(n)
            calc+=1
            if n==1:
                break
            if n%2==1:
                n=n*3+1
            else:n=int(n/2)
        print(calc)
    except EOFError:
        break
