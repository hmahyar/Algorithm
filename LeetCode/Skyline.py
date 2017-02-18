from heapq import *

class Solution:
    def getSkyline(self, LRH):
        result,H  = [],[]
        i, n = 0, len(LRH)
        while i < n or H:
            if not H or ((i < n) and (LRH[i][0] <= -H[0][1])):
                #print i,
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(H, (-LRH[i][2], -LRH[i][1]))
                    #print H,
                    i += 1
                #print 
            
            else:
                
                x = -H[0][1]
                #print 'End : ',x
                while H and -H[0][1] <= x:
                    heappop(H)

            
            height = len(H) and -H[0][0]
            if not result or height != result[-1][1]:
                result += [x, height],
        return result
                

print Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
#[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]