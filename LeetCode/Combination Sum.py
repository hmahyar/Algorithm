'''
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def Recu(target,nums,result,path,index=0):
            if target < 0:
                return
            
            if target  == 0:
                result.append(list(path))
                return
            else:
                for i in xrange(index,len(nums)):
                    Recu(target-nums[i],nums,result,path+[nums[i]],i)
                    
                    
        result, path = [],[]
        Recu(target,candidates,result, path,0)
        return result