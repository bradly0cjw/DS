n=input()
while(True):
    n=float(input())
    try:
        if(n=="nan"):
            print("NaN")
        else:
            n=1/n
            print("%.10g"%n)
    except:
        print("inf")
    
a=input()
while True:
    a=input()
    if a==("INf"):
        print(0)
    elif float(a)==(0):
        print("inf")
    elif a==("nan"):
        print("NaN")
    else:
        b=1/float(a)
        print('{:.6E}'.format(b))

