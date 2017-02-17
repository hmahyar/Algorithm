class Solution(object):
    def isMatch(self, s, p):
        T = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        T[0][0] = True


        for j in xrange(1,len(T[0])):
            if p[j-1]=='*': T[0][j] =T[0][j-2] 


        for i in xrange(1,len(s)+1):
            for j in xrange(1,len(p)+1):
                
                if p[j-1]==s[i-1] or p[j-1]=='.':
                    T[i][j] = T[i-1][j-1]
                
                elif p[j-1]=='*':
                    T[i][j] = T[i][j-2]
                    if s[i-1]==p[j-2] or p[j-2]=='.':
                        T[i][j] =T[i][j] | T[i-1][j]

        return T[-1][-1]