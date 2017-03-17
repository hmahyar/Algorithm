class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        D ={}
        if len(s)!=len(t):return False
        for i in s:
            if i not in D:D[i]=0
            D[i]+=1
        
        for j in t:
            if j in D: D[j]-=1
            else: D[j]= -1
            if D[j]<0: return False
        
        
        return True
        