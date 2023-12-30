# 3 sum
# leet code problem link:https://leetcode.com/problems/3sum/description/
'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

# using sort and binary search
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    target = 0
    n = len(nums)
    for i in range(n):
        if i!=0 and nums[i-1]==nums[i]:
            continue
        part_1 = nums[i]
        remain = target-part_1
        left = i+1
        right = n-1
        while(left<right):
            total = nums[left]+nums[right]

            if total == remain:
                result.append([nums[i],nums[left],nums[right]])
                left+=1
                while(left<right and nums[left-1]==nums[left]):
                    left+=1
            elif total<remain:
                left+=1
            else:
                right-=1
    return result