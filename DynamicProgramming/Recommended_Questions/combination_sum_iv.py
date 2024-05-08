# combination-sum-iv
# https://leetcode.com/problems/combination-sum-iv/description/
'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

'''

# Approach 1: Recursion (TLE)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def checktarget(total):
            if total<0:
                return 0
            
            if total==0:
                return 1
            
            count = 0
            for i in range(0,n):
                count += checktarget(total-nums[i])
            
            return count
        return checktarget(target)


# Approach 2: Dynamic Programming Top-Down Approach
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def checktarget(total):
            if total in memo:
                return memo[total]
            if total<0:
                return 0
            
            if total==0:
                return 1
            
            count = 0
            for i in range(0,n):
                count += checktarget(total-nums[i])
            memo[total] = count
            return memo[total]
        return checktarget(target)

# Approach 3: Dynamic Prgramming Bottom-Up
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for currSum in range(1,target+1):
            for currNum in nums:
                if currSum-currNum >= 0 :
                    dp[currSum]+=dp[currSum-currNum]
        return dp[target]
        