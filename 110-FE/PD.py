while 1:
    try:
        bitree=input().split()
        # print(bitree)
        dictionary=[]
        for x in range(len(bitree)):
            temp=[]
            if bitree[x]!="0":
                temp.append(bitree[x])
                tempx=x+1
                while tempx!=1:
                    if (tempx)%2==0:
                        temp.append(0)
                    else:
                        temp.append(1)
                    tempx=tempx//2
                temp.reverse()
                dictionary.append(temp)

        mount=int(input())
        for _ in range(mount):
            text=input()
            # print(dictionary)
            result=[]
            # print(text[0].isdigit(),text[0])
            if (not (text[0].isdigit())):
                for t in range(len(text)):
                    current=text[t]
                    encode=[]
                    for x in range(len(dictionary)):
                        if current==dictionary[x][-1]:
                            for y in range(len(dictionary[x])-1):
                                encode.append(dictionary[x][y])
                            result+=encode
                            # print(encode)
                            break
            else:
                decode=[]
                pointer=1
                for t in range(len(text)):
                    current=int(text[t])
                    # print(current,pointer,bitree[pointer*2+current-1],decode)
                    if bitree[pointer*2+current-1]!="0":
                        decode.append(bitree[pointer*2+current-1])
                        pointer=1
                    else:
                        pointer=pointer*2+current
                result+=decode
                pass
            for x in range(len(result)-1):
                print(result[x],end="")
            print(result[-1])
    except EOFError:
        break