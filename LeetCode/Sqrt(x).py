'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:return x
        l,r = 1,x/2
        while l<=r:
            mid =l+(r-l)/2
            if mid>x/mid: r=mid-1
            else: l= mid+1
        return l-1
        
