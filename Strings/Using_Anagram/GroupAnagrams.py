# Group Anagram
# LeetCode Link: https://leetcode.com/problems/group-anagrams/description/
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''

# Approach 1: Using sorting the string and collect all the strings matching the sorted string
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # hashmap to store the matching anagrams
    hashMap = {}
    #Iterate through strs array
    for i in range(len(strs)):
        # sort the string
        sortStr = ''.join(sorted(strs[i]))
        # check sorted string already exist in hashMap 
        if sortStr in hashMap.keys():
            # if exist add the string into array
            hashMap[sortStr].append(strs[i])
        else:
            # initialize the array with value
            hashMap[sortStr] = [strs[i]]
    
    # return the hashMap values for each key
    return list(hashMap.values())

# Approach 2: If we map each character to a prime number and we multiply each mapped number together, 
# anagrams should have the same multiple (prime factor decomposition)

# Get Prime number logic
def getPrimes():
    alphaPrimes = [0]*26
    alphaPrimes[0] = 2
    primes = 1
    i = 3
    while(primes<26):
        isPrime = False
        for j in range(2,i):
            if(i%j == 0):
                isPrime = True
        if(not isPrime):
            alphaPrimes[primes] = i
            primes+=1
        i+=1
    return alphaPrimes
        
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # get prime numbers for each character i.e 26 characters
    alphaPrimes = self.getPrimes()
    # hash map to group anagrams
    hashMap = defaultdict(list)
    # iterate through strs
    for i in range(len(strs)):
        # initial prime Multipier to calculate the total value of the string
        primeMulti = 1
        # calculate the total prime value of the string
        for c in strs[i]:
            primeMulti*=alphaPrimes[ord(c)-ord('a')]
        # add string into hashMap with primemuliplier of the string
        hashMap[primeMulti].append(strs[i])
    # return the values
    return list(hashMap.values())