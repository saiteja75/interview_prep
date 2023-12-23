# Palindromic Substrings
# LeetCode Problem Link: https://leetcode.com/problems/palindromic-substrings/description/
'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

# Method to check the substring is palindrome or not
def isPalindrome(val):
    # comparing substring with reverse of substring and return 1 if valid else 0
    return 1 if val == val[::-1] else 0

# Approach 1: Not soo efficient but useing two pointers
def countSubstrings(s: str) -> int:
        # Length of the string
        n = len(s)
        # result to count number of substrings
        count = 0

        # Loop of pointer 1 i.e i for start of substring
        for i in range(n):
            # Loop of pointer 2 i.e j for the remaining substring
            for j in range(i,n):
                # increment counter if subtrings within range of i to j is palindrome
                count+= isPalindrome(s[i:j+1])
        # return result
        return count


# Approach 2: Finding center and checking the substring palindromes
# Link: https://leetcode.com/problems/palindromic-substrings/solutions/2061497/python-easy-approach-beats-97/
def expandAndCountPallindromes(self, i, j, s):
        '''Counts the number of pallindrome substrings from a given center i,j        
        1. when i=j, it's an odd-lengthed pallindrome string. 
            eg: for string "aba", i=j=1.
        2. when i+1=j, it's an even-lengthed pallindrome string. 
            eg: for string "abba", i=1, j=2.
        
        Parameters:
            i,j - centers from which the code will expand to find number of pallindrome substrings.
            s - the string in which the code needs to find the pallindrome substrings. 
        
        Returns:
            cnt - The number of pallindrome substrings from the given center i,j       
        '''
        
        length=len(s)
        cnt=0
        
        while 0<=i and j<length and s[i]==s[j]:
            i-=1
            j+=1
            cnt+=1
        
        return cnt
        
def countSubstrings(self, s: str) -> int:
    return sum(self.expandAndCountPallindromes(i,i,s) + self.expandAndCountPallindromes(i,i+1,s) for i in range(len(s)))