'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''


class Codec:
    def serialize(self, root):
        def serializer(node):
            if node:
                result.append(str(node.val))
                serializer(node.left)
                serializer(node.right)
            else:
                result.append('*')
        result = []
        serializer(root)
        return ','.join(result)
        
    def deserialize(self, data):
        
        def desrializer():
            value = next(values)
            if value=='*':return None
            else:
                node = TreeNode(value)
                node.left = desrializer()
                node.right = desrializer()
                return node
                
        values = iter(data.split(','))
        return desrializer()
                    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
