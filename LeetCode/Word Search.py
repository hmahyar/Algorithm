'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


Time:  O(m * n * l)
Space: O(m * n)

'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        checker  = [[False for _ in xrange(len(board[0]))] for __ in xrange(len(board))]
        if len(word) > len(board) * len(board[0]): return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if  word[0] == board[i][j]:
                    if self.Discover(i,j,word,board,checker,0):
                        return True
        return False
        
    def Discover(self,i,j,word,board,checker,l):
            
            if len(word)==0:
                return True
            if  0<=i<len(board) and 0<=j<len(board[0]) and board[i][j]==word[0] and not checker[i][j]:
                checker[i][j] = True
                a = self.Discover(i+1,j,word[1:],board,checker,1) \
                       or self.Discover(i-1,j,word[1:],board,checker,2) \
                       or self.Discover(i,j+1,word[1:],board,checker,3) \
                       or self.Discover(i,j-1,word[1:],board,checker,4) 
                checker[i][j] = False
                return a
            
