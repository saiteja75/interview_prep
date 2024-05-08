# house-robber-ii
# https://leetcode.com/problems/house-robber-ii/description/
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police

'''

# Approach 1: Recursion (TLE)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def maxAmount(index, start):
            if index >=n:
                return 0
            
            currMax = 0
            for i in range(index+2,n):
                if start and i==n-1:
                    continue
                currMax = max(currMax,maxAmount(i,start))
            return nums[index]+currMax
        maxi = 0
        startIncluded = False
        for index in range(n):
            if index == 0:
                startIncluded = True
            maxi = max(maxi,maxAmount(index,startIncluded))
            startIncluded = False
        return maxi
        
# Approach 2: DP Top-Down
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def maxAmount(index, start):
            if (start,index) in memo:
                return memo[(start,index)]
            if index >=n:
                return 0
            
            currMax = 0
            for i in range(index+2,n):
                if start and i==n-1:
                    continue
                currMax = max(currMax,maxAmount(i,start))
            memo[(start,index)] = nums[index]+currMax
            return memo[(start,index)]
        maxi = 0
        startIncluded = False
        for index in range(n):
            if index == 0:
                startIncluded = True
            maxi = max(maxi,maxAmount(index,startIncluded))
            startIncluded = False
        return maxi
        