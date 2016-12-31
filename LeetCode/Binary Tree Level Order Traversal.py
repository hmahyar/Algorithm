# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q,result = [root],[]
        while q:
            level,nextlevel = [],[]
            for node in q:
                level.append(node.val)
                if node.left:nextlevel.append(node.left)
                if node.right:nextlevel.append(node.right)
            q=nextlevel
            result+=[level]
        return result
