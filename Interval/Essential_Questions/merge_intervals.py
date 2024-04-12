# merge-intervals
# https://leetcode.com/problems/merge-intervals/description/
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

# Approach 1: sort and check range of intervals
def merge(intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n == 1:
        return intervals
    intervals.sort(key=lambda a: a[0])
    res = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1,n):
        if start<=intervals[i][1] and end>=intervals[i][0]:
            end = max(end, intervals[i][1])
        else:
            res.append([start,end])
            start = intervals[i][0]
            end = intervals[i][1]
    res.append([start,end])
    return res