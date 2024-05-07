# longest-common-subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/
'''
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

'''

# Approach 1: Recursion (TLE)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        def lcs(index1,index2):
            if index1>=n or index2>=m:
                return 0
            
            if text1[index1] == text2[index2]:
                return 1+lcs(index1+1,index2+1)
            return max(lcs(index1,index2+1),lcs(index1+1,index2))
        return lcs(0,0)
        
# Approach 2: Dynamic Programming Top-Down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = {}
        def lcs(index1,index2):
            if (index1,index2) in memo:
                return memo[(index1,index2)]
            if index1>=n or index2>=m:
                return 0
            
            if text1[index1] == text2[index2]:
                memo[(index1,index2)] = 1+lcs(index1+1,index2+1)
                return memo[(index1,index2)]
            memo[(index1,index2)] = max(lcs(index1,index2+1),lcs(index1+1,index2))
            return memo[(index1,index2)]
        return lcs(0,0)

# Approach 3: Dynamic Programming Bottom-Up Approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        return dp[n][m]
        