# longest repeating character replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

# Approach: using sliding window and hash map
def characterReplacement(s: str, k: int) -> int:
    # variable to store maxlen after replacing the k characters
    maxLen = 1
    # left, right pointers for window
    left = 0
    right = 0
    # variable to store the frequency of occurance of the characters within the window
    countMap = {}
    # size of the string
    n = len(s)
    # iterate the string using right pointer
    while(right<n):
        # update the frequency of the current character
        countMap[s[right]] = 1 + countMap.get(s[right],0)
        # get the size of the window
        currSize = right-left+1
        # IMPORTANT LOGIC: 
        # 1. Get the highest frequency value of the character in the window 
        # 2. Negating the highest frequency from size of the window
        # 3. Check the negated result is less than or equal to k
        # 4. If condition satisfy then replacement is possible 
        if currSize-max(countMap.values()) <= k:
            # Update the maxLen
            maxLen = max(maxLen, currSize)
        else:
            # Since if condition is not satisfying we need to move the window to search for next possible combination
            # update the frequency by remove the start string
            countMap[s[left]]-=1
            # move the left to shift the window
            left+=1
        # increment the right
        right+=1
    # return the maxLen
    return maxLen