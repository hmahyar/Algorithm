'''
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        max_len = 0
        for string in wordDict:
            max_len = max(max_len, len(string))
        status = [False for _ in xrange(len(s)+1)]
        status[0]=True
        for p in xrange(1,len(s)+1):
            for l in xrange(1,min(p,max_len)+1):
                if status[p-l] and s[p-l:p] in wordDict:
                    status[p]=True
                    break
        print status
        return status[-1] 
