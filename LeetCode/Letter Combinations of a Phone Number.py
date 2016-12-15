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
