class Solution:
    def searchRange(self, nums, target):
        length=len(nums)
        list1=[]
        for i in range(length-1):
            if nums[i]==target:
                list1.append(i+1)
        return list1


if __name__=="__main__":
    num=[1,2,3,4,5]
    target=2
    position=Solution().searchRange(nums=num,target=target)
    print(position)