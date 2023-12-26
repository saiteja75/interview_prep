# range sum query immutable
# Leet Code Problem: https://leetcode.com/problems/range-sum-query-immutable/description/
'''
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = []
        total = 0
        # Storing the sum till that index in sum array
        for i in nums:
            total+=i
            self.sum.append(total)        

    def sumRange(self, left: int, right: int) -> int:
        # if left and right are non zero we just remove sum of left-1 from right which will give the sum from left to right
        if left > 0 and right > 0:
            return self.sum[right]-self.sum[left-1]
        # if left is zero just return sum[right] or if left and right are zero return sum[0]
        else:
            return self.sum[left or right]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)