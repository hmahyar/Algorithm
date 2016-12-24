'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 1 ≤ m ≤ length(nums) ≤ 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(nums,m,candidate):
            sum,result = 0,1
            for i in nums:
                sum+=i
                if (sum>candidate):
                    sum = i
                    result+=1
            return result<=m
                
        
        result_max, result_min = sum(nums), max(nums)
        while result_min<=result_max:
            mid = result_min+(result_max-result_min)/2
            if valid(nums,m,mid):
                result_max = mid-1
            else:
                result_min = mid+1 
            
        return result_min
