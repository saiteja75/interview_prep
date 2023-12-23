# Minimum Size Subarray Sum
# Leet Code Link: https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
'''

def minSubArrayLen(target: int, nums: List[int]) -> int:
        # two pointers for sliding window
        start,end = 0,0
        # Calculate the current sum within the window
        total = 0
        # Length of the array
        n = len(nums)
        # Result of min length sub array, initially assigning it too maximum value
        minLength = float('inf')

        # Iterating through the end till the length of the array
        while(end<n):

            # Adding the current pointer(index) value to the total
            total += nums[end]

            # If the condition of sum greater than equal to target it reached
            # calculate the minLength and also move the start pointer to decrease the window and check 
            # if still criteria matches calculate the minLength
            while(total>=target):
                # Calculate the minLength
                minLength = min(minLength,end-start+1)
                # removing the start pointer(index) value since we are moving out of the start and decreasing the window
                total-=nums[start]
                # increasing the start pointer
                start+=1
            
            # incrementing the end pointer to increase the window
            end+=1
        
        # if target value never reached return 0
        if minLength == float('inf'):
            return 0
        
        # return minimum length
        return minLength