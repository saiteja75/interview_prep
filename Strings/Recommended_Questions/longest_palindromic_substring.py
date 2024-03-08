# longest palindromic substring
# LeetCode Link: https://leetcode.com/problems/longest-palindromic-substring/description/
'''
Given a string s, return the longest 
palindromic substring in s.
'''

# Approach 1: using two pointer techniques in palindrome
def maxPalindromeSubstring(st,start,end,maxString):
    # pointer to move left side of the string
    i = start
    # pointer to move right side of the string
    j = end

    # compare the moving pointer values whether they are equal or not
    while i>=0 and j<len(st) and st[i] == st[j]:
        # update the maxString in current substring from i to j
        maxString = [st[i:j+1]] if (j-i+1)>len(maxString[0]) else maxString
        # move the pointer to left
        i-=1
        # move the pointer to right
        j+=1
    
    # return the maxString
    return maxString
        
def longestPalindrome(s: str) -> str:
    # to store the max sub-string
    maxString = ['']
    # length of the string
    n = len(s)
    # Iterate the string
    for i in range(n):
        # calculate max length sub-string with even length 
        even = maxPalindromeSubstring(s,i,i,maxString)
        # calculate max length sub-string with odd length 
        odd =  maxPalindromeSubstring(s,i,i+1,maxString)
        # compare odd and even and update max sub-string 
        if len(even[0])>len(odd[0]):
            maxString = even
        else:
            maxString = odd
    
    # return value
    return maxString[0]


# Approach 2: using dynamic Programming
# Solution: https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/
def longestPalindrome(s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str