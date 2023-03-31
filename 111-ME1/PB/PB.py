while 1:
    try:
        n=input()
        for i in range(0,len(n),3):
            a=n[i]
            b=n[i+1]
            c=n[i+2]
            print(chr(int(a+b+c)),end="")
        print()
    except EOFError:
        break