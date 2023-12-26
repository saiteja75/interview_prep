# Merge Intervals
# LeetCode Problem Link: https://leetcode.com/problems/merge-intervals/description/
'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that 
cover all the intervals in the input.
'''

# Approach: Sorting the list based on first element in the index and then merging
def merge(intervals: List[List[int]]) -> List[List[int]]:
    # length of the array
    n = len(intervals)
    # if the length is 1 just return the input as there is not need merge the intervals
    if n == 1:
        return intervals

    # Sorting the intervals based on the first element in the inner array
    intervals.sort(key=lambda val: val[0])
    # pointers to track the start and end of the interval
    start = intervals[0][0]
    end = intervals[0][1]
    # result of the merged interval
    result = []
    i = 1
    
    # iterate through array
    while(i<n):
        #LOGIC: is the end of the previous element is greater than the start of the current element
        if end >= intervals[i][0]:
            # Take the max of previous and current end element
            end = max(end, intervals[i][1])
        else:
            # Once there is no merge interval append it to the result
            result.append([start, end])
            # Update the pointers start and end with new values
            start = intervals[i][0]
            end = intervals[i][1]
        i+=1
    # Append the last interval
    result.append([start,end])
    
    # Return the result
    return result
