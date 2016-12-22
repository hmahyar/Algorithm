'''
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recu(num,stack,result):
			result.append(list(stack))
			for i in xrange(len(num)):
				stack.append(num[i])
				recu(num[i+1:],stack,result) 
				stack.pop()
        
        result = []
        recu(nums,[],result)
        return sorted(result,key=len) # Sorting is not necceserly 
