'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if len(matrix) == 1 and '1' in str(matrix[0]):
            return 1
            
        if len(matrix)<2 or len(matrix[0])<2:
           return 0 if len(matrix)==0 else max([int(i) for i in matrix[0]])

        max_size,max_i,max_j = 0,0,0
        C,R = len(matrix[0]) , len(matrix)
        M = [[0 for c in xrange(C)] for r in xrange(R)]
        for c in xrange(C):
            M[0][c] = int(matrix[0][c])
        max_size = max(M[0])
        
        
        
        for r in xrange(R):
            M[r][0] = int(matrix[r][0])
            max_size = max(M[r][0] ,max_size)
        for r in xrange(1,R):
            for c in xrange(1,C):
                if (matrix[r][c])=='1':
                    M[r][c] = min(int(M[r-1][c-1]),int(M[r-1][c]),int(M[r][c-1]))+1
                    if max_size < M[r][c]:
                        max_size = M[r][c]
                        max_i,max_j = r,c
                else:
                    M[r][c] = 0

        return max_size*max_size
                 
                
