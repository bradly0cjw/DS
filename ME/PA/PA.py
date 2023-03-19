while True:
    try:
        n=int(input())
        black=0
        sum=0
        result=0
        resultsum=0
        data=[1]
        for i in range(1,n):
            black+=(3**(i-1))
            if n==1:
                sum=1
            else:
                sum=(black*4)+1
            data.append(sum)
        result=data[-1]
        print(result)
        for a in data:
             resultsum+=a
        print(resultsum)
    except EOFError:
        break
