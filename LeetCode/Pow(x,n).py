'''
Implement pow(x, n).
'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result=1
        P_n = abs(n)
        while P_n:
            if P_n & 1:
                result*=x
            P_n >>=1
            x*=x
            
        return  1/result if n<0 else result


