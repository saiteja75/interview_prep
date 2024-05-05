# climbing-stairs
# https://leetcode.com/problems/climbing-stairs/description/
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

'''

# Approach 1: Recursion (TLE)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Approach 2: DP top-down
class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n < 0:
            return 0
        if n == 0:
            return 1
        memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]

# Approach 3: DP bottom-up
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[0] = 1
        memo[1] = 1
        for i in range(2,n+1):
            memo[i] = memo[i-1]+memo[i-2]
        return memo[n]