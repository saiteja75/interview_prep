# missing-number
# https://leetcode.com/problems/missing-number/description/
'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

'''

# Approach 1: math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        return (n*(n+1)//2)-total


# Approach 2: bit manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n+1):
            ans^=i
        
        for i in nums:
            ans^=i
        return ans
        