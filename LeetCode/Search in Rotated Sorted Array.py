'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , r  = 0,len(nums)-1
        while l<=r:
            mid  =  l+(r-l)/2
            if nums[mid]==target:return mid
            if nums[l]<=nums[mid]:
                if nums[mid]>target and nums[l]<=target: r = mid-1
                else: l = mid+1
            else:
                if nums[mid]<target and nums[r]>=target:  l=mid+1
                else: r= mid-1
        return -1
