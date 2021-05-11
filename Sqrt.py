import math

class Solution(object):
    def Mysqrt(self,x):
        return int(math.sqrt(x))

class Solution2(Solution):
    def __init__(self):
        super().__init__()

    def Mysqrt2(self,x):
        res = x
        while res * res > x:
            res = (res + x / res) / 2
        return int(res)

if __name__=="__main__":
    target=Solution2()

    print(target.Mysqrt2(10))