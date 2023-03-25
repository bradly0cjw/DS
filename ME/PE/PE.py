# n=list(map(str,input().split(" ",1)))
# n="8-(3+2*6)/5+4"
# n="(3+4)*5/(2-3)"
# n="(5*(3+2)-12)/(6-3)"
n=input()
stack=[]
out=[]
currnum=""

operater={'+':1,'-':1,'*':2,'/':2}
for i in range(len(n)):
    if n[i].isdigit():
        currnum=currnum+n[i]
        if i == len(n)-1 or not n[i+1].isdigit():
            out.append(currnum)
            currnum = ""
    else:
        if n[i] in "+-*/":
            while len(stack)>0 and stack[-1]!='(' and operater[n[i]]<= operater[stack[-1]]:
                out.append(stack.pop())
            stack.append(n[i])
        elif n[i]=="(":
            stack.append(n[i])
        elif n[i]==")":
            while stack[-1]!="(":
                out.append(stack.pop())
            stack.pop()

while len(stack)>0:
    out.append(stack.pop())
            
if len(out)>0:
    for y in range(len(out)-1):
        print(out[y],end=" ")
    print(out[-1])  

stack2=[]
while(len(out)>0):
    while out[0].isdigit():
        stack2.append(out[0])
        out.pop(0)
    if out[0] in "+-*/":
        b = int(stack2.pop())
        a = int(stack2.pop())
        if out[0] == "+":
            stack2.append(a + b)
        elif out[0] == "-":
            stack2.append(a - b)
        elif out[0] == "*":
            stack2.append(a * b)
        elif out[0] == "/":
            stack2.append(int(a / b))
        out.pop(0)
    if len(stack2)>0:
        for x in stack2:
            print(x,end=" ")
    if len(out)>0:
        for y in range(len(out)-1):
            print(out[y],end=" ")
        print(out[-1])    
