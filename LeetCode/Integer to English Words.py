'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

'''
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        lookup = {0: "Zero", 1:"One", 2: "Two", 3: "Three", 4: "Four", \
                  5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", \
                  10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", \
                  15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", \
                  20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", \
                  70: "Seventy", 80: "Eighty", 90: "Ninety"}
        units = ["", "Thousand", "Million", "Billion"]
		
        def _2digits(num):
            if num in lookup: return lookup[num]
            d,c = num//10 ,num%10
            if c:
                return lookup[d*10] +' '+ _2digits(c)
            return lookup[d]
            
        def _3digits(num):
            if num<100: return _2digits(num)
            d,c = num//100 ,num%100
            if c:
                return lookup[d]+' Hundred ' + _2digits(c)
            return lookup[d]+' Hundred'

        if num in lookup:return lookup[num]
        i,result = 0,[]
        while num:
            res = _3digits(num%1000)
            if num%1000 != 0: result.append(res+' '+units[i])
            num  = num//1000
            i+=1
        return ' '.join(result[::-1]).strip()
