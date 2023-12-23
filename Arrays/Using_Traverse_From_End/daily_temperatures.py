# Daily Temperatures
# LeetCode Problem Link: daily-temperatures
'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.

'''

#Appraoch 1: iterating from end and searching for the element greater than that
# NOTE THIS NOT EFFICIENT APPROACH
def dailyTemperatures(temperatures: List[int]) -> List[int]:
        # Length of the arr
        n = len(temperatures)
        # Creating the result array and initializing with 0
        result = [0]*n
        
        # Iterate from the end
        for i in range(n-1,-1,-1):
            # iterate from i to end as we have to find the next greater element
            for j in range(i,n):
                # if the we found the element greater that ith element calculate the difference in position
                if temperatures[j]>temperatures[i]:
                    # calculating the difference in position
                    result[i] = j-i
                    # Breaking since we have to find the first greater element than ith
                    break
        
        return result