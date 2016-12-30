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
