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
    return nums

def bubble_sorting(nums:List[int]):
    length=len(nums)
    print(length)
    list1=[]
    for i in range(8):
        list1.append(i)
    return list1

for i in range(10):
    print(i)

nums=[9,8,7,6,5,6,5,7]
# print(sortArray(nums=nums))

print(bubble_sorting(nums))

