
def reverse( x: int )->int:
    if '-' in str(x):
        x1 = -int(str(x)[1:][::-1])
    else:
        x1 = int(str(x)[::-1])
    if x1 < -2**31 or x1>2**31-1:
        return 0
    elif x1==0:
        return 0
    return x1


print(reverse(-32101))