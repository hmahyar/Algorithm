'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Time = O(n)
Space = O(n) , most of cases less than O(n)

'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        [1, -1, 5, -2, 3]
        """
        
        sum_zero_to_i = {}
        current_sum = 0
        result  = 0
        for i in nums:
            curent_sum += i 
            if current_sum == k: result=i+1
            elif current_sum - k in sum_zero_to_i : resutl = max(resutl , i-sum_zero_to_i[(current_sum - k)])
            if current_sum not in sum_zero_to_i:
                sum_zero_to_i[current_sum] = i
            return result
                
