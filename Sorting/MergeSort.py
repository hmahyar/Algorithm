class MergeSort(object):
    def __init__(self):
        pass

    def merge_sort(self,alist,start,end):
        if len(alist[start:end])<2:
                return alist[start:end]
        mid  = start+((end-start)//2)
        left = self.merge_sort(alist,start,mid)
        right =self.merge_sort(alist,mid,end) 
        
        result =[]
        while left and right:
            if left[0] >right[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        return result+left+right
    def merge_sort_3(self,alist,start,end):
        if len(alist[start:end])<2:
                return alist[start:end]
        mid  = start+((end-start)//2)
        left = self.merge_sort(alist,start,mid)
        right =self.merge_sort(alist,mid,end) 
        
        result =[]
        while left and right:
            if left[0] >right[0]:
                result.append(right.pop(0))
            else:
                result.append(left.pop(0))
        return result+left+right
                

msort= MergeSort()
alist = [1,3,5,7,9,2,4,3,6,9,0]
print msort.merge_sort(alist,0,len(alist)-1)

