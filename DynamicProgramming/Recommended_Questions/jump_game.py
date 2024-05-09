# jump-game
# https://leetcode.com/problems/jump-game/description/
'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

'''

# Approach 1: Recursion
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        def reachable(index):
            if index >= n or nums[index] == -1:
                return False
            if index == n-1:
                return True
            for i in range(0,nums[index]+1):
                nums[index] = -1
                if(reachable(index+i)):
                    return True
            return False
            
        return reachable(0)
            
        


# Approach 2: DP bottom up
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #using DP
        dp = [False] * len(nums) #create a DP every index i repsenet whther we can reach this index else False
        dp[0] = True #we aare already stading @ index 1

        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1): #for every index behind current index check if you can
                if nums[j] >= i - j and dp[j]:#reach current index from a previous index
                #above means from a prev step you can reach current step and we also need
                #to make sure we can reach that prev step so also checking dp[j]
                    dp[i] = True
                    break

        return dp[-1]
       
        