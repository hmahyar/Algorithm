'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

Show Company Tags
Show Tags

'''

class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                print i,j
                A[i][j], A[j][i] = A[j][i], A[i][j]

A  = [[1,2,3],[4,5,6]]
Solution().rotate(A)
print A
