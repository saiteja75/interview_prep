# Valid Anagrams
# https://leetcode.com/problems/valid-anagram/description/
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# GOOD REFERENCE: https://leetcode.com/problems/valid-anagram/solutions/3687854/3-method-s-c-java-python-beginner-friendly/

#Approach-1:
# Sort the two string and check both are equal or not
def isAnagram(s: str, t: str) -> bool:
        # sort the two string and return value
        return sorted(s) == sorted(t)

#Approach-2
# use hashmap to store the frequencies of the string 1 and then compare the occurances of string 2
def isAnagram(s: str, t: str) -> bool:
        # create a hashmap
        hashMap = {}
        # iterate through string 1
        for i in s:
            # add it into the hashMap if does not exist
            if hashMap.get(i,-1) == -1:
                hashMap[i] = 1
            # if already present increment the count of occurance
            else:
                hashMap[i]+=1
        # iterate through string 2
        for i in t:
            # if a new character occurs which is not present in string 1 return false
            if hashMap.get(i,-1) == -1:
                return False
            # if occurance found decrement the count
            else:
                hashMap[i]-=1
        # iterate through hashMap value
        for i in hashMap.values():
            # if any value is not zero then there is a extra occurance so return false
            if i!=0:
                return False
        # if every condition is satisfied return true
        return True