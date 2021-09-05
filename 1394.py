from typing import List
import collections

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = collections.Counter(arr)
        # 先按频次排序，再按数值大小排序
        res = sorted(cnt.items(), key=lambda x:(x[1],x[0]), reverse=True)
        for i in range(len(res)):
            # 频次等于数值大小
            value0=res[i][0]
            value1=res[i][1]
            if res[i][0] == res[i][1]:
                return res[i][0]
        return -1

class solution(Solution):
    def findLucky(self, arr: List[int]):
        length=len(arr)
        print(length)
        result=dict()
        for i in range(0,length-1):
            count = 1
            for j in range(i+1,length):
                if arr[i]==arr[j]:
                    count+=1
            result[arr[i]]=count
        return result

if __name__=="__main__":
    target=solution().findLucky(arr=[1,1,4,2,1,2,2,3])
    print(target)