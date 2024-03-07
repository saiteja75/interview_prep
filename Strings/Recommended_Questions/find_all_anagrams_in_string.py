# find all anagrams in a string
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# Approach 1: using sliding window and sorting
def findAnagrams(s: str, p: str) -> List[int]:
    n = len(s)
    m = len(p)
    p = ''.join(sorted(p))
    result = []
    left = 0
    right = 0
    while(right<n):
        if right>=m-1:
            srt = ''.join(sorted(s[left:right+1]))
            if srt == p:
                result.append(left)
            left+=1
        right+=1
    return result


# Approach 2: using Sliding Window and hash Map
def findAnagrams(s: str, p: str) -> List[int]:
    pFrqMap = {}
    for i in p:
        pFrqMap[i] = 1+pFrqMap.get(i,0)
    subMap = {}
    left = 0
    right = 0
    n = len(s)
    m = len(p)
    result = []
    while(right<n):
        if s[right] not in pFrqMap.keys():
            left = right+1
            subMap = {}
        else:
            window = right-left
            subMap[s[right]] = 1+subMap.get(s[right],0)
            if window >= m-1:
                if pFrqMap == subMap:
                    result.append(left)
                subMap[s[left]]-=1
                left+=1
        right+=1
    if pFrqMap == subMap:
        result.append(left)
    return results