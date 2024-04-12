# insert-interval
# https://leetcode.com/problems/insert-interval/description/
'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
'''

def insert( intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    
    for interval in intervals:
        # the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
        if interval[1] < newInterval[0]:
            result.append(interval)
        # the new interval's range is before the other, so we can add the new interval and update it to the current one
        elif interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval
        # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval 
        elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(newInterval[1], interval[1])

    
    result.append(newInterval); 
    return result

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        res = []
        intervals.append(newInterval)
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        n = n+1

        for i in range(1,n):
            if start<=intervals[i][1] and end>=intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start,end])
        return res
        