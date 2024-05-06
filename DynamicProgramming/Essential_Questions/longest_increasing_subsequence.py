# longest-increasing-subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/description/
'''
Given an integer array nums, return the length of the longest strictly increasing 
subsequence

'''

# Approach 1: recursion (TLE)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def maxLength(index):
            if index>=n:
                return 0
            maxi = 0
            for i in range(1,n):
                if index+i<n and nums[index]<nums[index+i]:
                    maxi = max(maxi,maxLength(index+i))
            return 1+maxi
        
        maxi = 1
        for i in range(n):
            maxi = max(maxi,maxLength(i))
        return maxi


# Approach 2: Dynamic Programming Top-Down
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def maxLength(index,memo):
            if index in memo:
                return memo[index]
            if index>=n:
                return 0
            maxi = 0
            for i in range(1,n):
                if index+i<n and nums[index]<nums[index+i]:
                    maxi = max(maxi,maxLength(index+i,memo))
            memo[index] = 1+maxi
            return memo[index]
        
        maxi = 1
        memo = {}
        for i in range(n):
            maxi = max(maxi,maxLength(i,memo))
        return maxi


# Approach 3: Dynamic Programming Bottom-Up
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)] 
        dp[n-1]=1
        maxi = dp[n-1]
        for i in range(n-2,-1,-1):
            for j in range(1,n):
                if i+j<n and nums[i] < nums[i+j]:
                    dp[i] = max(dp[i],dp[i+j])
            dp[i]+=1
            maxi = max(maxi,dp[i])
        return maxi