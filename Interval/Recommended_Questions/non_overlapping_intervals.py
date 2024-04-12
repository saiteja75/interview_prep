# non-overlapping-intervals
# https://leetcode.com/problems/non-overlapping-intervals/description/
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

'''

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    n = len(intervals)
    if n == 1:
        return 0
    intervals.sort(key = lambda val:val[1])
    count = 0
    end =  intervals[0][1]
    i = 1
    while(i<n):
        if end > intervals[i][0]:
            count+=1
        else:
            end = intervals[i][1]
        i+=1

    return count