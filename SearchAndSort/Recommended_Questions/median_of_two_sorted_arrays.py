# median-of-two-sorted-arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
'''

# Approach 1: create new arr and get median
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    arr = []

    i = 0
    j = 0
    while(i<m and j<n):
        if(nums1[i]<=nums2[j]):
            arr.append(nums1[i])
            i+=1
        else:
            arr.append(nums2[j])
            j+=1
    while(i<m):
        arr.append(nums1[i])
        i+=1

    while(j<n):
        arr.append(nums2[j])
        j+=1
    
    size = m+n
    if((size)%2):
        return arr[(size)//2]
    else:
        return (arr[(size)//2]+arr[((size)//2)-1])/2
    

# Approach 2: binary search on one array and checking the mid of the whole array
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums2)<len(nums1):
        return self.findMedianSortedArrays(nums2,nums1)
    n = len(nums1)
    m = len(nums2)
    total = n+m
    half = total//2
    l = 0
    r = n-1
    while True:
        mid1 = l+(r-l)//2
        mid2 = half-mid1-2

        mid1Left = nums1[mid1] if mid1>=0 else float('-inf')
        mid1Right = nums1[mid1+1] if mid1+1<n else float('inf')
        mid2Left = nums2[mid2] if mid2>=0 else float('-inf')
        mid2Right = nums2[mid2+1] if mid2+1<m else float('inf')

        if(mid1Left<=mid2Right and mid2Left<=mid1Right):
            if(total%2):
                return min(mid1Right,mid2Right)
            else:
                return (max(mid1Left,mid2Left)+min(mid1Right,mid2Right))/2
        
        if(mid1Left > mid2Right):
            r = mid1-1
        else:
            l = mid1+1