'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
TIme= O(nlogn)
'''

class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals)==0:return 0
        starts = sorted(intervals,key = lambda x:x.start)
        ends = sorted(intervals,key = lambda x:x.end)
        result,sp,ep,maxnumber=0,0,0,0
        while sp<len(starts):
            if starts[sp].start<ends[ep].end:
                result+=1
                sp+=1
                maxnumber = max(maxnumber,result)
            else:
                result-=1
                ep+=1

        return maxnumber
                
