# permutations
# https://leetcode.com/problems/permutations/description/
'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

'''

#Approach 1: backtrack
def permute(nums: List[int]) -> List[List[int]]:
    res = []
    def compute(arr,nums,res):
        if(len(arr[:]) == len(nums)):
            res.append(arr[:])
            return

        for i in range(0,len(nums)):
            if( nums[i] in arr):
                continue
            arr.append(nums[i])
            compute(arr,nums,res)
            arr.pop()
    
    compute([],nums,res)
    return res