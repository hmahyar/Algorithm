'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Time = O(n^2) + O(nlogn) = O(n^2)
Space = O(1)
'''
class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		nums = sorted(nums) #O(nlogn)
		result = []
		for i in xrange(len(nums)-2):
			if i>0 and nums[i]==nums[i-1]: continue # skip duplicate items
			b,e = i+1,len(nums)-1
			while b<e:
				#print b,i,e
				if nums[b]+nums[i]+nums[e]<0: b+=1
				elif nums[b]+nums[i]+nums[e]>0: e-=1
				else: 
					result.append([nums[i],nums[b],nums[e]])
					b,e=b+1,e-1
					while b<e and nums[b] == nums[b-1]:b+=1
					while b<e and e<len(nums)-1 and nums[e] == nums[e+1]:e-=1
		return result
