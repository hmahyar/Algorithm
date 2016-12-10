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
