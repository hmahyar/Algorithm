'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in map:
                stack.append(i)
                continue
            if len(stack)==0 or map[stack.pop()]!=i:
                return False
        return len(stack)==0 
