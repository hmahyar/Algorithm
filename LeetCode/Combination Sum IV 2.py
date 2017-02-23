def combinationSum4(nums,target):
    if target == 0:
        return 1
    
    res = 0
    i=0
    while i < len(nums):
        if (target >= nums[i]):
            res += combinationSum4(nums, target - nums[i])
        i+=1
    return res


print combinationSum4([1,2],3)