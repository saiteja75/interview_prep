# two sum
# leetcode link: https://leetcode.com/problems/two-sum/description/
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

# Approach: usng hashMap and subtracting the target
from collections import defaultdict

def twoSum(nums: List[int], target: int) -> List[int]:
    # initialize result array
    result = [-1,-1]
    # create a hashMap with -1 as inital value for each key
    numStore = defaultdict(lambda: -1)
    # iterate the arr
    for i in range(len(nums)):
        # calculate the remain value after substracting the current index value from target
        remain = target-nums[i]
        # fetch the index for remain value
        index = numStore[remain]
        # if index is not -1 and index does not match with current index
        # then that is the result
        if index!=-1 and index!=i:
            # update result
            result[0] = i
            result[1] = index
            # since we need only one pair break the loop
            break
        # add the current value into the hashMap
        numStore[nums[i]] = i
    return result 
        