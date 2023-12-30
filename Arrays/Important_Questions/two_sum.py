# two sum
# LeetCode Link: https://leetcode.com/problems/two-sum/description/
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

#Approach: two pass using hashmap
def twoSum(nums: List[int], target: int) -> List[int]:
        # creating a hash map to store index with its element
        numIndex = dict()
        # iterating and updating the hashmap
        for i in range(len(nums)):
            numIndex[nums[i]] = i
        # iterate and search for target pair
        for i in range(len(nums)):
            # check whether there is element in hashmap of target-numspi
            remain = numIndex.get(target - nums[i],-1)
            # if exist and its not the same index return the pair
            if remain>-1 and remain != i:
                return [i, remain]


#Approach: one pass using hashmap         
def twoSum( nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return [] 