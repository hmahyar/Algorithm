'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        def merge(a,b):
            l1 = l2 = ListNode(None)
            while a and b:
                if a.val<b.val:l1.next,a = a,a.next
                else:l1.next, b = b, b.next
                l1 = l1.next
            l1.next = a or b
            return l2.next
         
        if len(lists)==0: return []
        while len(lists)>1:
            lists.append(merge(lists.pop(0),lists.pop(0)))
        return lists[-1]
