# kth-largest-element-in-an-array
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
'''

# Approach 1: Sorting
def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[len(nums)-k]


#Approach 2: Quick Select (similar approach of quick Sort)
# take a pivort node
# place it in its position such that left part of the array is less than pivort node
# right part of the array is greater than pivort node
def findKthLargest(nums: List[int], k: int) -> int:
    k = len(nums)-k
    l = 0
    r = len(nums)-1
    def quickSelect(l,r):
        pivort = r
        p = l
        for i in range(l,r):
            if nums[i]<nums[pivort]:
                nums[p],nums[i] = nums[i],nums[p]
                p+=1
        nums[p],nums[pivort] = nums[pivort],nums[p]

        if(p<k): return quickSelect(p+1,r)
        elif(p>k): return quickSelect(l,p-1)
        else:
            return nums[p]
    return quickSelect(l,r)