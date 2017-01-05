'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''

class Solution:
    def largestRectangleArea(self, height):
        increasing, area, i = [], 0, 0
        while i <= len(height):
            if not increasing or (i < len(height) and height[i] > height[increasing[-1]]):
                
                increasing.append(i)
                #print '1->',increasing,i
                i += 1
            else:
                last = increasing.pop()
                if not increasing:
                    #print '2->',increasing,i,height[last] * i
                    area = max(area, height[last] * i)
                else:
                    #print '3->',increasing,i,height[last] * (i - increasing[-1] - 1 ),increasing[-1]
                    area = max(area, height[last] * (i - increasing[-1] - 1 ))
        return area

if __name__ == "__main__":
    print Solution().largestRectangleArea([6,4,6,5])