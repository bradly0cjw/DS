# while True:
#     n=int(input())
#     f1=1
#     f2=1
#     if n==1 or n==2:
#         print(1)
#     else:
#         for i in range(n-2):
#             temp=f1+f2
#             f1=f2
#             f2=temp
#         print(temp)

def hanoi(n,a,b,c):
    if n==1:
        print("move 1 from %c to %c\n"%(a,c))
    else:
        hanoi(n-1,a,c,b)
        print("move %d from %c to %c\n"%(n,a,c))
        hanoi(n-1,b,a,c)
while True:
    A,B,C=str("A"),str("B"),str("C")
    N=int(input())
    if N==0:
        print("there are no fucking disk")
    else:
        hanoi(N,A,B,C)