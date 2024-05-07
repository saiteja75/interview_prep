# partition-equal-subset-sum
# https://leetcode.com/problems/partition-equal-subset-sum/description/
'''
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

'''

# Approach 1: Recursion (TLE)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 or n<2:
            return False
        target = total//2
        def checkSubSet(index,target):
            if index>=n:
                return False
            
            if target==0:
                return True
            
            return  checkSubSet(index+1,target-nums[index]) or checkSubSet(index+1,target)
        return checkSubSet(0,target)
        
# Approach 2: Dynamic Programming Top-Down Approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 or n<2:
            return False
        target = total//2
        dp = [[-1 for i in range(target+1)] for _ in range(n)]
        def checkSubSet(index,target,dp):
            if index>=n:
                return False
            
            if dp[index][target] != -1:
                return dp[index][target]
            if target==0:
                return True
            
            dp[index][target] = checkSubSet(index+1,target-nums[index],dp) or checkSubSet(index+1,target,dp)
            return dp[index][target]
        return checkSubSet(0,target,dp)

# Approach 3: Dynamic Programming Bottom-Up Approach
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1:
            return False
        """
        The dp array stores the total obtained sums we have come across so far.
        Notice that dp[0] = True; if we never select any element, the total sum is 0.
        """
        dp = [True]+[False]*s
        # Now, loop through each element
        for num in nums:
            for curr in range(s, num-1, -1):  # avoid going out-of-bounds
                """
                Case 1: The current sum (curr) has been seen before.
                        Then, if we don't select the current element, the sum will not change.
						So, this total sum will still exist, and its dp value remains True.
				
				Case 2: The current sum (curr) has not been seen before,
				        but it can be obtained by selecting the current element.
						This means that dp[curr-num] = True, and thus dp[curr] now becomes True.
				
				Case 3: The current sum (curr) has not been seen before,
				        and it cannot be obtained by selecting the current element.
						So, this total sum will still not exist, and its dp value remains False.
                """
                dp[curr] = dp[curr] or dp[curr-num]
        # Finally, we want to obtain the target sum
        return dp[s//2]  # or dp[s>>1]