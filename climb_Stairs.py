class Solution(object):
    def climbStairs(self,x:int):
        sum=0
        if x<=2:
            return x
        else:
            sum+=self.climbStairs(x-1)
            sum+=self.climbStairs(x-2)
            return sum

if __name__=="__main__":
    target=Solution()
    print(target.climbStairs(5))

