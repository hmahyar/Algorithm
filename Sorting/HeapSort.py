class HeapSort(object):
  def __init__(self):
    pass

  def heap_sort(self,alist):
    length = len(alist)-1
    last_parent = length//2
    while last_parent>-1:
        self.heapify(alist,last_parent,length)
        last_parent-=1
    for i in xrange(length,0,-1):
      if alist[0]>alist[i]:
        alist[0],alist[i]= alist[i],alist[0]
        self.heapify(alist,0,i-1)


  def heapify(self,alist,root,last):
    l_child = root*2+1
    while last>=l_child:
      if last>l_child and alist[l_child]<alist[l_child+1]:l_child+=1
      if alist[l_child]>alist[root]:
        alist[l_child],alist[root] = alist[root],alist[l_child]
        root = l_child
        l_child=2*root+1
      else:
        break


h= HeapSort()
alist = [5,2,6,9,2,3,0,-1]
h.heap_sort(alist)
print alist