from typing import List

def sortArray(nums: List[int]) -> List[int]:
    nums.sort()
    return nums

def sortArray_algorithm(nums: List[int]) -> List[int]:
    arrayLength=len(nums)
    print(nums)
    for i in range(0,arrayLength):
        for j in range(i+1,arrayLength):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
                print(nums)
    return nums

nums=[9,8,7,6,5,6,5,7]
# print(sortArray(nums=nums))

print(sortArray_algorithm(nums))