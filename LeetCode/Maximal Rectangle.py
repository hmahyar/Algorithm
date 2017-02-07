'''
Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 6.

______________________________________________________________________________________________________________
The DP solution proceeds row by row, starting from the first row. Let the maximal rectangle area at row i and column j be computed by [right(i,j) - left(i,j)]*height(i,j).

All the 3 variables left, right, and height can be determined by the information from previous row, and also information from the current row. So it can be regarded as a DP solution. The transition equations are:

left(i,j) = max(left(i-1,j), cur_left), cur_left can be determined from the current row
right(i,j) = min(right(i-1,j), cur_right), cur_right can be determined from the current row
height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';
height(i,j) = 0, if matrix[i][j]=='0'



If you think this algorithm is not easy to understand, you can try this example:

0 0 0 1 0 0 0 
0 0 1 1 1 0 0 
0 1 1 1 1 1 0
The vector "left" and "right" from row 0 to row 2 are as follows

row 0:

l: 0 0 0 3 0 0 0
r: 7 7 7 4 7 7 7
row 1:

l: 0 0 2 3 2 0 0
r: 7 7 5 4 5 7 7 
row 2:

l: 0 1 2 3 2 1 0
r: 7 6 5 4 5 6 7
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        result = 0
        
        if not matrix:return result
        m,n = len(matrix),len(matrix[0])
        L =  [0]*len(matrix[0]) #left  boundary
        R =  [n]*len(matrix[0]) #right boundry
        H =  [0]*len(matrix[0]) #hight 
        for i in xrange(m):
            left,right = 0,n
            for j in xrange(n):
                if matrix[i][j]=='1':
                    L[j] = max(L[j],left)
                    H[j]+=1
                else:
                    L[j],H[j],R[j]=0,0,n
                    left=j+1
            for j in reversed(xrange(n)):
                if matrix[i][j]=='1':
                    R[j] = min(R[j],right)
                    result = max(result,H[j]*(R[j]-L[j]))
                else:
                    right = j
        return result
            
            