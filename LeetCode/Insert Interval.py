'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result,i = [],0
        while i < len(intervals) and newInterval.start > intervals[i].end:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:
            newInterval = Interval(min(newInterval.start, intervals[i].start),max(newInterval.end, intervals[i].end))
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result
