class Node(object):
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
	
	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class Link_List(object):
	def __init__(self):
		self.head=self.end = None
	
	def add(self,item):
		temp = Node(item)
		if self.head == None:
			self.head =self.end= temp
			self.head.setNext(self.end)
		else:
			self.end.setNext(temp)
			self.end = temp
		
	def get_all(self):
		curent = self.head
		while curent!= None:
			print curent.getData()
			curent = curent.getNext()
	
	def search(self,item):
		curent = self.head
		while curent!= None:
			if item == curent.getData():
				return True
			curent = curent.getNext()
		return False
llist= Link_List()
llist.add('A')
llist.add('B')
print 'C',llist.search('C')
print 'B',llist.search('B')


