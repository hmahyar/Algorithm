'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root: return []
        stack,result=[[root,'']],[]
        while stack:
            #print stack
            node,path = stack.pop()
            path+=str(node.val)+'->'
            if node.left:
                stack.append([node.left,path])
            if node.right:
                stack.append([node.right,path])
            if not node.right and not node.left:
                result.append(path[:-2])
        return result
