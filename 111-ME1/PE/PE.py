def Arithmetic(num, s, result=None):
    if result is None:
        result = []
    if s == 0:
        for x in num:
            result.append(x)
    else:
        add = int(num[0]) + int(num[1])
        subtract = int(num[0]) - int(num[1])
        newa = [add] + num[2:]
        news = [subtract] + num[2:]
        Arithmetic(newa, s-1, result)
        Arithmetic(news, s-1, result)
    return result

n = int(input())

for i in range(n):
    s = int(input())
    num = list(map(int, input().split()))
    result = Arithmetic(num, s-1)
    result.sort(reverse=True)
    result2 = []
    for x in result:
        if x not in result2:
            result2.append(x)
    print(*result2)