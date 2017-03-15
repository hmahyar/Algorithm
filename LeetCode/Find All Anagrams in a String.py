'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s==None or len(s)==0 or p==None or len(p)==0:return []
        hash,result = {},[]
        for c in p:
            if c not in hash:hash[c]=0
            hash[c]+=1
        l,r,count = 0,0,len(p)
        while r<len(s):
            
            if  s[r] in hash: 
                if hash[s[r]]>0: count-=1
                hash[s[r]]-=1
            r+=1
            
            if count==0: result.append(l)
            
            if r - l == len(p):
                
                if (s[l] in hash) and (hash[s[l]]>=0):
                    count+=1
                if s[l] in hash:hash[s[l]]+=1
                l+=1
        return result 