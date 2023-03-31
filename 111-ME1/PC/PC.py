while 1:
    try:
        n=input().split()
        m=list(map(int,input().split()))
        command=[]
        cmd=n[1]
        for i in range(0,len(cmd)):
            command.append(cmd[i])
        data=m[:]
        calc=[]
        tcalc=[]

        while len(command)>0:
            for x in data:
                if x!=0:
                    calc.append(x)
            if command[0]=='L':
                while len(calc)>1:
                    a=calc[0]
                    b=calc[1]
                    if a==b:
                        calc.pop(0)
                        calc.pop(0)
                        tcalc.append(a+b)
                    else:
                        tcalc.append(a)
                        calc.pop(0)
                if len(calc)>0:
                    tcalc.append(calc.pop(0))
                while len(tcalc)<int(n[0]):
                    tcalc.append(0)
            elif command[0]=='R':
                while len(calc)>1:
                    a=calc[-1]
                    b=calc[-2]
                    if a==b:
                        calc.pop(-1)
                        calc.pop(-1)
                        tcalc.append(a+b)
                    else:
                        tcalc.append(a)
                        calc.pop(-1)
                if len(calc)>0:
                    tcalc.append(calc.pop(-1))
                while len(tcalc)<int(n[0]):
                    tcalc.append(0)
                tcalc=tcalc[::-1]
            data=tcalc[:]
            tcalc.clear()
            command.pop(0)
        print(*data)
    except EOFError:
        break