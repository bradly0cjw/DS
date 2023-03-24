# n=input()
# def word(arr):
#     if len(arr)>0:
#         data=[]
#         for x in arr:
#             data.append(x)
#         for i in range(0,len(data)):
#             print(data[i],end="")
#             data.pop(i)
#             return word(data)
#     else:
#         print()
#         return
# word(n)

## This code is Fixed by Chat GPT
n=input()
def word(arr, prefix=""):
    if len(arr) == 0:
        print(prefix)
    else:
        for i in range(len(arr)):
            new_prefix = prefix + arr[i]
            new_arr = arr[:i] + arr[i+1:]
            word(new_arr, new_prefix)

word(n)