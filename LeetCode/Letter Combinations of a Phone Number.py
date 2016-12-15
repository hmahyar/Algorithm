'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.


Time= O(4n) ,n is number of digits in input number.
'''


class Solution:
    # @return a list of strings, [s1, s2]
    def __init__(self):
    	self.lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    def letterCombinations(self, digits):
        self.result = []
        self.Recu(digits,'',0)
        return [item for item in self.result if item!='']

    def Recu(self,digits,com,lev):
    	if len(digits)==lev:
    		self.result.append(com)
    	else:
    		for item in self.lookup[int(digits[lev])]:
    			self.Recu(digits,com+item,lev+1)

                
