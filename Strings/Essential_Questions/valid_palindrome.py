# Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/description/
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

# Approach 1
# Remove non alpha and numeric character and reverse the string anc check its palindrome or not
def isPalindrome(s: str) -> bool:
        # create a variable with store filtered string
        filteredStr = ''
        # iterate the string
        for i in s:
            # if the character is alpha num add it in filteredStr
            if i.isalnum():
                # make it lowercase and append to the string
                filteredStr+=i.lower()
        # compare by reversing the string
        return filteredStr == filteredStr[::-1]

# Approach 2
# Remove non alpha and numeric character and compare start and end
def isPalindrome(s: str) -> bool:
        # create a variable with store filtered string
        filteredStr = ''
        # iterate the string
        for i in s:
            # if the character is alpha num add it in filteredStr
            if i.isalnum():
                # make it lowercase and append to the string
                filteredStr+=i.lower()
        #initialze the start and end
        start = 0
        end = len(filteredStr)-1
        while(start<end):
            # if start and end not matching then its not a palindrome return false
            if filteredStr[start] != filteredStr[end]:
                return False
            start+=1
            end-=1
        # if every character matching from start and end return true
        return True

# Approach-3
# same as approach 2 without extra space
def isPalindrome(s: str) -> bool:
        start = 0
        end = len(s)-1
        while(start<end):
            if s[start].isalnum() and s[end].isalnum() and s[start].lower() != s[end].lower():
                return False
            elif s[start].isalnum() != True:
                start+=1
            elif s[end].isalnum() != True:
                end-=1
            else:
                start+=1
                end-=1

        return True