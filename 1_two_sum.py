def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    sorted_id = sorted(range(len(nums)), key=lambda k: nums[k]) #排序
    head = 0
    tail = len(nums) - 1
    sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    while sum_result != target:
        if sum_result > target:
            tail -= 1
        elif sum_result < target:
            head += 1
        sum_result = nums[sorted_id[head]] + nums[sorted_id[tail]]
    return [sorted_id[head], sorted_id[tail]]



num=[9,8,7,6,5]
x=range(len(num))
print(x)


target=15
result=twoSum(nums=num,target=target)
print(result)

