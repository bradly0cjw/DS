
i=float(0.54900000000000000)
def roundup(x,presion=0):
    print(x%(10**presion))
    if (x%(10**presion))>=0.5*(10**presion):
        return (x//(10**presion))*(10**presion)+(10**presion)
    else:
        return (x//(10**presion))*(10**presion)
print(roundup(i,-2))
# print(i*10)
print(round(i,-2))