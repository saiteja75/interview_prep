# unique-paths
# https://leetcode.com/problems/unique-paths/description/
'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

'''

# Approach 1: Recursion (TLE)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def countPath(row,col):
            if row>=m or col>=n:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            return countPath(row+1,col)+countPath(row,col+1)
        return countPath(0,0)
        
# Approach 2: DP top-down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def countPath(row,col):
            if (row,col) in memo:
                return memo[(row,col)]
            if row>=m or col>=n:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            memo[(row,col)] = countPath(row+1,col)+countPath(row,col+1)
            return memo[(row,col)]
        return countPath(0,0)

# Approach 3: DP bottom-up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if j-1>=0:
                    dp[i][j] += dp[i][j-1]
                if i-1>=0:
                    dp[i][j] += dp[i-1][j]
        return dp[m-1][n-1]
        
        