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
                
