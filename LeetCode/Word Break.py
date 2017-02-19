'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        if len(wordDict)==0: return False
        max_len = max(wordDict)
        status = [False for _ in xrange(len(s)+1)]
        status[0]=True
        
        for p in xrange(1,len(s)+1):
            for l in xrange(1,min(p,max_len)+1):
                if status[p-l] and s[p-l:p] in wordDict:
                    status[p]=True
                    break
        print status
        return status[-1]    
                