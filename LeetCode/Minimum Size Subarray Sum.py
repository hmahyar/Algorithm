'''
Given an array of n positive integers and a positive integer s, find the minimal length
of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
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
