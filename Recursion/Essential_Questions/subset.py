# subsets
#  https://leetcode.com/problems/subsets/description/
'''
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
'''

# Approach: Recursion with backtracking
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def compute(arr,index,res,nums):
        res.append(arr[:])
        if(index == len(nums)):
            return
        
        for i in range(index,len(nums)):
            arr.append(nums[i])
            compute(arr,i+1,res,nums)
            arr.pop()
    compute([],0,res,nums)
    return res


# Approach: {MORE REFINED) Recursion with backtracking
def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    def compute(arr,index,res,nums):
        
        if(index == len(nums)):
            res.append(arr[:])
            return
            
        arr.append(nums[index])
        compute(arr,index+1,res,nums)
        arr.pop()
        compute(arr,index+1,res,nums)
    compute([],0,res,nums)
    return res