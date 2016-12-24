'''
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result,temp,start = float('inf'),0,0
        for i in xrange(len(nums)):
            temp+=nums[i]
            while temp>=s:
                result = min(result,(i-start)+1)
                temp-=nums[start]
                start+=1
        return result if result!=float('inf') else 0
