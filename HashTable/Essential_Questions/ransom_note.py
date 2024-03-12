# ransom note
# leetcode problem Link: https://leetcode.com/problems/ransom-note/description/
'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

from collections import defaultdict
def canConstruct(ransomNote: str, magazine: str) -> bool:
    # size of the two inputs
    n = len(magazine)
    m = len(ransomNote)
    # if ransomNote size is more than magazine return false
    if m>n:
        return False
    # initialze the result
    result = True
    # creata hashMap with initial value of zero
    charMap = defaultdict(lambda: 0)
    # Update the frequence of each character in the hashMap
    for i in range(n):
        charMap[magazine[i]] +=1
    # iterate the ransome
    for i in range(m):
        # check if the ransom  character is not present in hashMap return false and stop loop
        if charMap[ransomNote[i]] == 0:
            result = False
            break
        # update the hashMap by subtract the value as this character is used up
        charMap[ransomNote[i]]-=1
    return result
    
    