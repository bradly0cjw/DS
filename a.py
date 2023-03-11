while True:
    a=input().split(' ')
    mod=int(a[0])
    div=int(a[1])
    b=int(mod)
    status=0
    if (div==0):
        print("Boring!")
    elif (div==1):
        print("Boring!")
    else:
        while (b!=1):
            b=(b)/div
            if (b%1)!=0:
                status=1
                break
        if status==0:
            while(mod!=1):
                print(int(mod),end=" ")
                mod=mod/div
            print(1)
        else:
            print("Boring!")

