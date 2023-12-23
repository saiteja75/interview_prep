# Merge Sorted Array
# LeetCode Problem LinK: https://leetcode.com/problems/merge-sorted-array/description/
'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
''' 

# Approach 1: sorting b arrays always after each swap
def merge( a: List[int], m: int, b: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # two pointers one pointing to a arr and other pointing to b arr 
    i,j = 0,0

    # Iterate the two arrays parallely
    while(i<m and j<n):
        # if value in a is more we need to swap the value
        if a[i]>b[j]:
            # Swap the lower value from b to a since we need to store all the values in a  
            a[i],b[j] = b[j],a[i]
            # need sort b array because the incoming value can be greater or less than remaining value so we have to sort it
            b.sort()
    # fill remaining b array values in a array
    for k in range(n):
            a[k+m] = b[k]

# Approach 2: starting from end of the arrays and start placing it end of arr a
# Link: https://leetcode.com/problems/merge-sorted-array/solutions/3436053/beats-100-best-c-java-python-and-javascript-solution-two-pointer-stl/
def merge(nums1, m, nums2, n):
        # Pointer i in arr a(nums1) starting from end
        i = m - 1
        # Pointer j in arr b(nums2) starting from end
        j = n - 1
        # pointer to end of the combined arr a,b
        k = m + n - 1
        
        # iterating util we traverse arr b
        while j >= 0:
            # Check we did not completely traverse arr a
            # if number in arr a is greater than number in arr b
            if i >= 0 and nums1[i] > nums2[j]:
                # place it end pointer k in arr a
                nums1[k] = nums1[i]
                # decrement i as we have processed that value
                i -= 1
            else:
                # place it end pointer k in arr a
                nums1[k] = nums2[j]
                # decrement j as we have processed that value
                j -= 1
            # decrement k as it expected value is filled
            k -= 1