'''
Given two strings S and T, determine if they are both one edit distance apart.
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        bi,sm = len(s),len(t)
        if bi<sm: return self.isOneEditDistance(t, s)
        if bi-sm>1: return False
        i=0
        while i<sm and t[i]==s[i]: i+=1
        if bi-sm==0: i+=1
        while i<sm and t[i]==s[i+(bi-sm)]: i+=1
        return i==sm
