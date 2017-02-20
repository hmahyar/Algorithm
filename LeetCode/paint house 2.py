class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs : return 0
        
        n = len(costs)
        m = len(costs[0])
        c = [costs[0],[0]*m]
        ans = 0

        for i in xrange(1,n):
            F_m , S_m = float('inf'), float('inf')
            
            for j in xrange(m):
                if c[(i-1)%2][j] < F_m:   F_m,S_m = c[(i-1)%2][j],F_m
                elif c[(i-1)%2][j] < S_m: S_m = c[(i-1)%2][j]
                    
            for j in xrange(m):
                min_ = F_m if F_m !=c[(i-1)%2][j] else S_m
                c[i%2][j] = min_ + costs[i][j]
        
        return min(c[(n-1)%2])


print Solution().minCostII([[1,5,3],[2,9,4]])





