# binary-search
# https://leetcode.com/problems/binary-search/description/
'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''


def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while(left<=right):
        mid = left+(right-left)//2

        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            right = mid-1
        else:
            left = mid+1
    return -1