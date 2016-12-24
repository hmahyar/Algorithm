

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def F1(i,seq):
            result,j  ='',0
            while j<len(seq[i]):
                counter = 1
                while j<len(seq[i])-1 and seq[i][j]==seq[i][j+1]: 
                    counter+=1
                    j+=1
                result+=(str(counter)+str(seq[i][j]))
                j+=1
            return result 
            
        seq = ['1']
        [seq.append(F1(i,seq)) for i in xrange(n-1)]
        return seq[-1]
