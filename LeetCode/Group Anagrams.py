'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs==[""]:return [strs]
        A = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st in A: A[sorted_st].append(st)
            else: A[sorted_st] = [st]

        result = []
        [result.append(A[item]) for item in A]
        return result
