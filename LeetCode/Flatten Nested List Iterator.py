
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList,0]]

    def next(self):
        """
        :rtype: int
        """
        self.hasNext()
        lst,i = self.stack[-1]
        self.stack[-1][1]+=1
        return lst[i]

    def hasNext(self):
        """
        :rtype: bool
        """
        s = self.stack
        while s:
            lst,i = s[-1]
            if i==len(lst):
                s.pop()
            else:
                if type(lst[i])==int:
                    return True
                s[-1][1]+=1
                s.append([lst[i],0])
        return False

        
nl = NestedIterator([[1,1],2,[1,1]])
while nl.hasNext():
    print nl.next()


