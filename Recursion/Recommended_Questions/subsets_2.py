# subsets-ii
# https://leetcode.com/problems/subsets-ii/description/
'''
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# approach 1: backtrack
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def compute(arr,index,nums,res):
        if(index == len(nums)):
            if arr[:] not in res:
                res.append(arr[:])
            return
        
        arr.append(nums[index])
        compute(arr,index+1,nums,res)
        arr.pop()
        compute(arr,index+1,nums,res)
    compute([],0,nums,res)
    return res

# Approach 2: [MORE OPTIMIZED] back track
def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    def compute(arr,index,nums,res):
        if(index == len(nums)):
            res.append(arr[:])
            return
        arr.append(nums[index])
        compute(arr,index+1,nums,res)
        arr.pop()
        # skipping the possible duplicates
        while( index+1<len(nums) and nums[index] == nums[index+1]):
            index+=1
        compute(arr,index+1,nums,res)
    compute([],0,nums,res)
    return res
        
        