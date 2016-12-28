'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.
'''

class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node
            
    def delete(self, node):
        if node.prev: node.prev.next = node.next
        else:         self.head = node.next
        if node.next: node.next.prev = node.prev
        else:         self.tail = node.prev
        del node

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.LRU = LinkedList()
        self.capacity = capacity
        

    def get(self, key):
        """
        :rtype: int
        """
        
        if key not in self.dict: return -1
        newnode = ListNode(key,self.dict[key].val)
        self.LRU.insert(newnode)
        self.LRU.delete(self.dict[key])
        self.dict[key] = newnode
        return newnode.val
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            self.LRU.delete(self.dict[key])
        elif len(self.dict)>=self.capacity:
            oldnode = self.LRU.head
            self.LRU.delete(self.LRU.head)
            del self.dict[oldnode.key]

        newnode = ListNode(key,value)
        self.LRU.insert(newnode)
        self.dict[key] = newnode
        


    


