import math
def B2D(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[-i-1]*(2**i)
    return sum
while 1:
    try:
        n=input()
        binary=[]
        temp=int(n)
        while 1:
            binary.append(temp%2)
            if (temp//2==0):
                break
            else:
                temp=temp//2
        binary.reverse()
        a1=binary[:math.ceil(len(binary)/2)]
        a2=binary[math.ceil(len(binary)/2):]
        b1=binary[:int((len(binary)/3))]
        b2=binary[int((len(binary)/3)):int((len(binary)/3))*2]
        b3=binary[int((len(binary)/3))*2:]
        count=1
        # for x in binary:
        #     print(x,end="")
        #     if count==12:
        #         print("@",end="")
        #         count=1
        #     else:
        #         count+=1
        # print()
        # print(*b1,"@",*b2,"@",*b3)
        h1=[]
        for i in range(len(a1)):
            h1.append(a1[i]^a2[i])
        h2=[]
        for i in range(len(b1)):
            h2.append((b1[i]^b2[i])^b3[i])
        lh1=int((len(h1)-len(n))/2)
        lh2=int((len(h2)-len(n))/2)
        h1=h1[lh1:lh1+len(n)]
        h2=h2[lh2:lh2+len(n)]
        # for x in h1:
        #     print(x,end="")
        # print()
        # for x in h2:
        #     print(x,end="")
        # print()      
        print(B2D(h1),B2D(h2))
    except EOFError:
        break