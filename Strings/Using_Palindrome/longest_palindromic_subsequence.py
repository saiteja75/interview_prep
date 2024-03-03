# longest palindromic subsequence
# LeetCode Problem: https://leetcode.com/problems/longest-palindromic-subsequence/
'''
!!!!!!!!!!!!!!!! NEED TO UNDERSTAND PLEASE REVISE !!!!!!!!!!!!!!!!!!
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
'''

def longestPalindromeSubseq(self, s: str) -> int:
        dp = []
        for i in range(len(s)):
            temp = []
            for j in range(len(s)):
                temp.append(0)
            dp.append(temp)

        for i in range(len(s)-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1,len(s)):
                if(s[i] == s[j]):
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]
        

'''
Debugger Logs:
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 1]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
[[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 1, 3], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
[[1, 0, 0, 0, 0], [0, 1, 2, 2, 3], [0, 0, 1, 1, 3], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
[[1, 2, 3, 3, 4], [0, 1, 2, 2, 3], [0, 0, 1, 1, 3], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1]]
'''
