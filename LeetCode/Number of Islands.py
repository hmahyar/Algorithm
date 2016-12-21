```
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
```



class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.path_check,result= [[False for __ in xrange(len(grid[0]))] for _ in xrange(len(grid))],0

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j]=='1' and not self.path_check[i][j]:
                    self.discover(i,j,grid)
                    result+=1
        return result
        
    def discover(self,i,j,grid):
            if grid[i][j]== '0' or self.path_check[i][j]: return
            self.path_check[i][j]=True
            if i<len(grid)-1: self.discover(i+1,j,grid)
            if i>0: self.discover(i-1,j,grid)
            if j<len(grid[0])-1: self.discover(i,j+1,grid)
            if j>0: self.discover(i,j-1,grid)
