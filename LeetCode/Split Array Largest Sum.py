'''
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty 
continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

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

____________________________________________________________________
Solution: 
1) the maximum answer(biggest answer) regardless of input m is sum of the input nums, 
and the minimum possibple answer regardless of input m is biggest number in nums list 
2) checking a possible answer is easy. assume we have a candidate we just wanted to make sure weather it is working or not
3) so this question it is a really simple bineary search, we have maximum possible answer and minumum possible answer
we just need to apply a binary search to see if our candidate weather is valin or not 


Time = O(nlogn), n= biggest pisiibility or sum of nums
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
