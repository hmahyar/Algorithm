'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, history = 1,{key:0 for key in nums}
        for i in nums:
            if history[i]!=0: continue
            L,R=  history.get(i-1,0),history.get(i+1,0)
            length = L+R+1
            result ,history[i-L],history[i+R],history[i] = max(result,length),length,length,length
        return result
        
