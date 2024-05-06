# house-robber
# https://leetcode.com/problems/house-robber/description/
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

'''

# Approach 1: Recursion (TLE)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def maxAmount(index):
            if index>=n:
                return 0
            maxi = 0
            for j in range(2,n):
                maxi = max(maxi,maxAmount(index+j))
            return nums[index]+maxi
        
        if n<=2:
            return max(nums)
        maxiTotal = 0
        for i in range(0,n):
            maxiTotal = max(maxiTotal,maxAmount(i))
        return maxiTotal

                
# Appraoch 2: Dynamic Programming Top-Down Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def maxAmount(index,memo):
            if index in memo:
                return memo[index]
            if index>=n:
                return 0
            maxi = 0
            for j in range(2,n):
                maxi = max(maxi,maxAmount(index+j,memo))
            memo[index] = nums[index]+maxi
            return memo[index]
        
        if n<=2:
            return max(nums)
        maxiTotal = 0
        memo =  {}
        for i in range(0,n):
            maxiTotal = max(maxiTotal,maxAmount(i,memo))
        return maxiTotal

                
# Approach 3: Dynamic Programming Bottom-Up Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)] 
        dp[n-1]=nums[n-1]
        maxi = dp[n-1]
        for i in range(n-2,-1,-1):
            for j in range(i+2,n):
                dp[i] = max(dp[i],dp[j])
            dp[i]+=nums[i]
            maxi = max(maxi,dp[i])
        return maxi