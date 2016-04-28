class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits)-1
        overflow = 1
        
        while i >-1:
            if digits[i]+overflow>9:
                digits[i] = (digits[i]+overflow) % 10
                overflow =1
            else:
                digits[i] = (digits[i]+overflow)
                overflow =0
            i-=1
        if overflow!=0:
            return [1]+digits
        return digits

s = Solution()
print s.plusOne([0])