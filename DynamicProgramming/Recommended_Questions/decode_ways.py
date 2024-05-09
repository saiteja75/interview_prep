# decode-ways
# https://leetcode.com/problems/decode-ways/description/
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

 

'''

# Approach 1: Recursion (TLE)
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        def countDecodes(index,s):
            if index == n:
                return 1
            if s[index] == '0':
                return 0
            count = countDecodes(index+1,s)
            if index<n-1 and (s[index]=='1' or (s[index]=='2' and s[index+1]<'7')):
                count+=countDecodes(index+2,s)
            return count
        
            
        return countDecodes(0,s)

# Approach 2: Dp top-down
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo = {}
        def countDecodes(index,s):
            if index in memo:
                return memo[index]
            if index == n:
                return 1
            if s[index] == '0':
                return 0
            count = countDecodes(index+1,s)
            if index<n-1 and (s[index]=='1' or (s[index]=='2' and s[index+1]<'7')):
                count+=countDecodes(index+2,s)
            memo[index] = count
            return memo[index]
        
            
        return countDecodes(0,s)

# Approach 3: Dp bottom-up
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if s[0] == "0":
            return 0
        dp = [0 for _ in range(n+1)]
        dp[n] = 1
        
        for index in range(n-1,-1,-1):
            if s[index] == '0':
                dp[index] = 0
            else:
                dp[index] = dp[index+1]
                if(index<n-1 and (s[index]=='1' or s[index]=='2' and s[index+1]<'7')):
                     dp[index]+=dp[index+2]
        return dp[0]