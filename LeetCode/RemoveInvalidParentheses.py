'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
'''

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.remove(s,0,0,result,['(',')']) 
        return result
        
    def remove(self,s,last_i,last_j,result,sign):
            sum = 0
            for i in xrange(last_i,len(s)):
                if s[i]==sign[0]: sum+=1
                if s[i]==sign[1]: sum-=1
                if sum>=0: continue
                for j in xrange(last_j,i+1):
                    if s[j]==sign[1] and (j == last_j or s[j]!=s[j-1]):
                        self.remove(s[:j]+s[j+1:],i,j,result,sign)
                return
            
            s = s[::-1]
            if sign[0]=='(': self.remove(s,0,0,result,[')','('])
            else: result.append(s)

#if __name__ == "__main__":

print Solution().removeInvalidParentheses('(()()))')





