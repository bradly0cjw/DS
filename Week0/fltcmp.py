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
    
