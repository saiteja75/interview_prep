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

#Appraoch 2: using Stack
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures) # having list with 0`s elements of same lenght as temperature array.
    stack = [] # taking empty stack. 
    for index, temp in enumerate(temperatures): # Traversing through provided list. 
        while stack and temperatures[stack[-1]] < temp: # stack should not be empty and checking previous temp with current temp. 
            # the above while loop and taking stack for saving index is very common practice in monotonic stack questions. Suggestion: understand it properly. 
            prev_temp = stack.pop() # stack.pop() will provide index of prev temp, taking in separate var as we are using it more then on place. 
            result[prev_temp] = index - prev_temp #at the index of prev_temp and i - prev_temp by this we`ll get how many step we moved to have greater temp. 
        stack.append(index) # in case stack is empty we`ll push index in it. 

    return result # returing the list of number of days to wait. 