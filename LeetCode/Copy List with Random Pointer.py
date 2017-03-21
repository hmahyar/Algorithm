'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        
        node = head
        while node:
            copy = RandomListNode(node.label)
            copy.next = node.next
            node.next = copy
            node = copy.next
            
        
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next
        
        
        temp = RandomListNode(0)
        c_current, current = temp, head
        while current:
            c_current.next = current.next
            current.next = current.next.next
            c_current ,current = c_current.next,current.next
            

        return temp.next