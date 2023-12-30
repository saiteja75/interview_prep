# maximum subarray
# LeetCode Problem LinK: https://leetcode.com/problems/maximum-subarray/description/
'''
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
'''

def maxSubArray(self, nums: List[int]) -> int:
    # to add the element in array
    total = 0
    # For Tracking the max sum sub-array
    maxSum = float('-inf')

    # iterate the arrays
    for value in nums:
        # Add the element value
        total+=value

        # Update the maxSum if needed
        maxSum = max(total,maxSum)

        # if current sub-array sum is less than zero
        if total < 0:
            # reset the total to 0 to track next max sub-array
            total = 0
    
    # return the maxSum
    return maxSum