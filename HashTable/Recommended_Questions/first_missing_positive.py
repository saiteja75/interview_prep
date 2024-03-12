# first  missing  positive
# LeetCode Problem: https://leetcode.com/problems/first-missing-positive/description/
'''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

'''

# Approach: Using hashMap
def firstMissingPositive(nums: List[int]) -> int:
    countHash = {}
    for i in nums:
        if countHash.get(i,-1) == -1:
            countHash[i] = 1
        else:
            countHash[i]+=1

    maxEle = float('-inf')
    
    for i in nums:
        maxEle = max(maxEle, i)
    
    if maxEle <=0:
        return 1

    for i in range(1, maxEle+1):
        if i>0 and countHash.get(i,-1) == -1:
            return i
        return maxEle+1
    
#Approach2: Optimal Solution
def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)

    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1