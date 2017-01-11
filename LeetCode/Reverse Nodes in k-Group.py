'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
     def tra(self,end=None):
         while self:
            if self==end:break
            print self.val,'->',
            self=self.next
             

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp =ListNode('*')
        temp.next = head
        
        head_p,temp_p = head,temp
        length =1
        print '\n',temp.tra()
        while head_p:
            p3 = head_p.next # Save next Node to P3
            if  length % k==0:
                #print '\n',temp.tra(),head_p.val,head_p.next.val,temp_p.val
                p4 = temp_p.next
                self.reverse(temp_p,head_p.next)
                temp_p = p4
                print '\n',temp.tra(),head_p.val,temp_p.val,p4.val
            head_p = p3 # Move Forward- updateing curnt node with next node
            length+=1
        #temp.tra()
        return temp.next
        
    def reverse(self, begin, end):
            first = begin.next
            cur = first.next
            
            while cur != end:
                first.next = cur.next
                cur.next = begin.next
                begin.next = cur
                cur = first.next
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print Solution().reverseKGroup(head, 3)
                    
                    
                    
            
            
        
        
        
        