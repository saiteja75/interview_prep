# search in rotated sorted array
# LeetCode problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''
here is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

# Using low bound concept of binary search
def search(nums: List[int], target: int) -> int:
    # low and high for binary search
    low = 0
    high = len(nums)-1

    # cutting down the array to find the target
    while(low<=high):
        # taking the middle index
        mid = (low+high)//2

        # check if current middle is the targets
        # if yes return index
        if nums[mid] == target:
            return mid

        # check if low index value is less that mid index value
        # that means it left part is sorted
        if nums[low]<=nums[mid]:
            # check is the tarhget lies in the range of low and mid
            # search in this range
            # else move into the right part of the array
            if nums[low]<=target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
        # checking in the right part of the array
        else:
            # if the target is in range of mid and high
            # search in that range
            # else move to left part of the array
            if nums[mid]<target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    # if target is not present return -1
    return -1