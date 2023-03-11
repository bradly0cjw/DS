n=int(input())
if n>0 or n<=100:
    for i in range(n):
        time=0
        a=input()
        while True:
            x=0
            for j in range(len(a)):
                x=x+(int(a[len(a)-j-1]))*(10**(len(a)-j-1))
            if (int(a)-x)==0:
                break
            a=str(int(a)+int(x))
            time=time+1
            if time>1000:
                break
        if time<=1000:
            print(str(time)+" "+str(a))