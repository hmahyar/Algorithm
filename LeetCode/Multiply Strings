
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.

'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        '''
        99
        99
        __
        48
       120
       ___
       168
        '''
        result = [0 for _ in xrange(len(num1)+len(num2))]
        num1 , num2 = num1[::-1],num2[::-1]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                result[i+j] += int(num1[i])*int(num2[j])
                result[i+j+1] += result[i+j] /10
                result[i+j] %=10
        
        k = len(result)-1
        while k>0 and result[k]==0:
            k-=1
            
            
        return  ''.join(map(str,result[k::-1]))
            
                
        
