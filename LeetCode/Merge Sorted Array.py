'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional
elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l, a,b = m+n-1, m-1 , n-1
        while a>=0 and b>=0:
            if nums1[a]>nums2[b]:
                nums1[l] = nums1[a]
                a-=1
            else:
                nums1[l] = nums2[b]
                b-=1
            l-=1
        while b>=0:
            nums1[l] = nums2[b]
            b-=1
            l-=1
