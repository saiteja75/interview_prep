# longest substring without repeating characters
# LeetCode Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Given a string s, find the length of the longest 
substring
 without repeating characters.
'''

# Approach ONE: Using HashMap
def lengthOfLongestSubstring(s: str) -> int:
        # length of the string
        n = len(s)
        # two pointer for sliding window
        start,end = 0,0
        # Maximum length of substring without repeating characters
        maxLength = 0
        # hash map to track the characters with its latest occuring index 
        charMap = {}

        # if n is 0 or 1 return the length
        if n == 0 or n == 1:
            return n

        # increment end to increase the size of the window and track non-repeating characters
        while(end<n):
            # if the character is already occured we need cut down the window size
            # How to decide till which index it should be cut down?
            # if the current repeating character is occurred after the window start we should update the start pointer to it and add plus one to skip repeated
            # if the current repeating character is occurred before the window start no need to upate the start
            if charMap.get(s[end],-1)>-1:
                start = max(charMap[s[end]]+1,start)
            # update repeated character index in the hashMap
            charMap[s[end]] = end
            # Now start and end pointers are in range of non-repeating character calculate the MaxLength
            maxLength = max(maxLength,end-start+1)
            # increase the window size
            end+=1
        return maxLength

#Approach TWO: using hashset
def lengthOfLongestSubstring(s: str) -> int:
        # length of the string
        n = len(s)
        # two pointer for sliding window
        start,end = 0,0
        # Maximum length of substring without repeating characters
        maxLength = 0
        #Hashset
        hashSet = set()
        
        while(end<n):
            if s[end] not in hashSet:
                hashSet.add(s[end])
                end+=1
                maxLength = max(maxLength,end-start+1)
            else:
                 hashSet.remove(s[start])
                 start+=1
        
        return maxLength
            
