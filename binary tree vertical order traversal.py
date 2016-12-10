'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.


Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]


Time=  O(n)
Space= O(n)
'''




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        result,order,stack = {}, 0, [[0,root]]
        while stack:
            order,node = stack.pop(0)
            if order in result:result[order].append(node.val)
            else:result[order] = [node.val]
            if node.left: stack += [order-1, node.left],
            if node.right: stack += [order+1, node.right],
        return  [result[i] for i in xrange(min(result), max(result) + 1)]
