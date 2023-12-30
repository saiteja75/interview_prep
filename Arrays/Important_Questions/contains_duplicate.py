# contains duplicate
#LeetCode Problem LinK: https://leetcode.com/problems/contains-duplicate/description/
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

# Approach 1: using hash set
def containsDuplicate(nums: List[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True

# Approach 2: using hahsmap
def containsDuplicate(nums: List[int]) -> bool:
    hashMap = {}
    for i in nums:
        if hashMap.get(i,-1) == -1:
            hashMap[i] = 1
        else:
            return True
    return False

# Approach 3: using sorting
def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    print(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False