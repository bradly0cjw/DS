count=1
while True:
    try:
        n=int(input())
        print("Case %d:"%count,end="")
        tr=0
        b=0
        m=0
        t=0
        h=0
        if n>1000000000000:
            tr=n//1000000000000
            n=n%1000000000000
        if n>1000000000:
            b=n//1000000000
            n=n%1000000000
        if n>1000000:
            m=n//1000000
            n=n%1000000
        if n>1000:
            t=n//1000
            n=n%1000
        if n>100:
            h=n//100
            n=n%100
        if tr>0:
            if tr>=100:
                trh=tr//100
                trc=tr%100
                if trc>0:
                    print(" %d hundred %d trillion"%(trh,trc),end="")
                else:
                    print(" %d hundred trillion"%(trh),end="")
            else:
                print(" %d trillion"%(tr),end="")
        if b>0:
            if b>=100:
                bh=b//100
                bc=b%100
                if bc>0:
                    print(" %d hundred %d billion"%(bh,bc),end="")
                else:
                    print(" %d hundred billion"%(bh),end="")
            else:
                print(" %d billion"%(b),end="")       
        if m>0:
            if m>=100:
                mh=m//100
                mc=m%100
                if mc>0:
                    print(" %d hundred %d million"%(mh,mc),end="")
                else:
                    print(" %d hundred million"%(mh),end="")
            else:
                print(" %d million"%(m),end="")
        if t>0:
            if t>=100:
                th=t//100
                tc=t%100
                if tc>0:
                    print(" %d hundred %d thousand"%(th,tc),end="")
                else:
                    print(" %d hundred thousand"%(th),end="")
            else:
                print(" %d thousand"%(t),end="")
        if h>0:
            print(" %d hundred"%(h),end="")
        if n>0:
            print(" %d"%(n),end="")
        if tr==0 and m==0 and b==0 and t==0 and h==0 and n==0:
            print(" 0",end="")
        print()
        count+=1
    except EOFError:
        break