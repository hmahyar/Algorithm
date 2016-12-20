'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

Time = O(nlogn)
Space = O(1)
'''


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<2: return intervals
        intervals = sorted(intervals,key=lambda x:x.start)
        i=1
        while i<len(intervals):
            if intervals[i].start<=intervals[i-1].end:
                intervals[i-1].end = max(intervals[i].end,intervals[i-1].end)
                intervals.pop(i)
            else: i+=1
        return intervals
