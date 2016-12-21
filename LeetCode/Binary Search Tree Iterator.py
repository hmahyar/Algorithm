'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.s,self.p = [],root
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.s or self.p
        
        

    def next(self):
        """
        :rtype: int
        """
        
        while self.p:
            self.s.append(self.p)
            self.p = self.p.left
        result  = self.s.pop()
        self.p = result.right
        return result.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
