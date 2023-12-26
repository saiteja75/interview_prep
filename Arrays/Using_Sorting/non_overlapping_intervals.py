# non overlapping intervals
# LeetCode Problem Link: https://leetcode.com/problems/non-overlapping-intervals/description/
'''
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
'''

# Approach: sorting the intervals based on th second element in each index value
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # length of the array
        n = len(intervals)
        # if the length is 1 just return the input as there is not need merge the intervals
        if n == 1:
            return 0
        
        # Sorting the intervals based on the second element in the inner array be we are talking about removing intervals
        intervals.sort(key = lambda val:val[1])

        # result value as we have tell how many intervals we have to remove
        count = 0
        # previous element end value
        end =  intervals[0][1]
        i = 1
        # iterate array
        while(i<n):
            # if the end of previous element is greater than current start element there is possible merge
            # so increment the counter
            if end > intervals[i][0]:
                count+=1
            else:
                # track of the previous end element
                end = intervals[i][1]
            i+=1

        # return the count
        return count