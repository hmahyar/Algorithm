'''
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
________________________________________________________________________________________________________________________
Solution
comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].
fact: comb[0]=1

EX :
nums = [1,2] , target = 2
comb[2] => sum(comb[2-1],comb[2-2]) => sum(comb[1],comb[0]) => sum(comb[1-1],comb[0]) => sum(comb[0],comb[0])  => sum(1,1) => 2
'''

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        history = [0]*(target+1)
        history[0]=1
        nums = sorted(nums)
        
        for i in xrange(1,target+1):
            for j in xrange(len(nums)):
                if nums[j]<=i: history[i]+=history[i-nums[j]]
        return history[-1]
