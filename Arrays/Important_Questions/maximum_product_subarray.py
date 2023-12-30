# maximum product subarray
# LeetCode Problem: https://leetcode.com/problems/maximum-product-subarray/description/
'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
'''

# Approach 1: Prefix and Postfix product
def maxProduct(nums: List[int]) -> int:
    # initialize prefix and postfix with one
    pre,suf = 1,1
    # To store max value while calculate the max value
    maxValue = float('-inf')
    # Length of the array
    n = len(nums)
    # iterate the rray
    for i in range(n):
        # if there is any element which is 0 will end up pree and post product to zero
        # so we need to reset values to 1 so we can continue calclate subarray product
        if pre == 0:
            pre = 1
        if suf == 0:
            suf = 1
        # product of subarray from start and end
        pre *= nums[i]
        suf *= nums[n-i-1]
        # Update the maxValue in the current index by taking max from pre and post
        maxValue = max(maxValue,max(pre,suf))
    
    # return maxvalue
    return maxValue

# Approach 2:  prefix product in different way
def maxProduct(self, nums: List[int]) -> int:
    ## RC ##
    ## APPROACH : KADANES ALGORITHM ##
    
    ## TIME COMPLEXITY : O(N) ##
    ## SPACE COMPLEXITY : O(1) ##
    
    # 1. Edge Case : Negative * Negative = Positive
    # 2. So we need to keep track of minimum values also, as they can yield maximum values.
    
    global_max = prev_max = prev_min = nums[0]
    for num in nums[1:]:
        curr_min = min(prev_max*num, prev_min*num, num)
        curr_max = max(prev_max*num, prev_min*num, num)
        global_max= max(global_max, curr_max)
        prev_max = curr_max
        prev_min = curr_min
    return global_max 