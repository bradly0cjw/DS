b=int(input())
for i in range(b):
    a=input()
    if a==("INf"):
        print(0)
    elif float(a)==(0):
        print("inf")
    elif a==("nan"):
        print("NaN")
    else:
        print(1/float(a))
