class QucikSort(object):
    def __init__(self):
        pass
    def quick_sort(self,alist,first,last):
        if first<last:
            pivot = self.partition(alist,first,last)
            self.quick_sort(alist,first,pivot-1)
            self.quick_sort(alist,pivot+1,last)

    def partition(self,alist, first,last):
        pivot_value ,pivot_index,done= alist[first],first,False
        first+=1
        while not done:
            while first<=last and alist[first]<=pivot_value:first+=1   
            while last>=first and alist[last]>=pivot_value: last-=1     
            if first>last:done = True
            else:alist[first],alist[last]= alist[last],alist[first]
        alist[pivot_index],alist[last] = alist[last],alist[pivot_index]
        return last                

    def quick_sort_3way(self,alist,first,last):
        if last-first<2: return
        key = alist[first]
        f=r = first
        e = last
        while r<e:
            if alist[r]<key:
                alist[f],alist[r] = alist[r],alist[f]
                f+=1
                r+=1
            elif alist[r]==key:
                r+=1
            else:
                e-=1
                alist[e],alist[r] = alist[r],alist[e]
        self.quick_sort_3way(alist,first,f)
        self.quick_sort_3way(alist,e,last)


qsort = QucikSort()
alist = [5,3,2,4,7,5,9,8,0,0,1]
qsort.quick_sort_3way(alist,0,len(alist))
print alist


alist = [5,3,2,4,7,5,9,8,0,0,1]
qsort.quick_sort(alist,0,len(alist)-1)
print alist

