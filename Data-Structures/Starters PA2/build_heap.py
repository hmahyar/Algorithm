# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
      length  = len(self._data)-1
      i = length//2
      for i in range(i,-1,-1):
        self.heapify(i,length)

  def heapify(self,i,length):
      biggetstchild = (i*2)+1
      
      while length>=biggetstchild:
        if biggetstchild<length and self._data[biggetstchild]>self._data[biggetstchild+1]:biggetstchild+=1
        if self._data[i]>self._data[biggetstchild]:
          self._swaps.append([i,biggetstchild])
          self._data[i],self._data[biggetstchild]=self._data[biggetstchild],self._data[i]
          i = biggetstchild
          biggetstchild = (i*2)+1
        else:
          break

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
