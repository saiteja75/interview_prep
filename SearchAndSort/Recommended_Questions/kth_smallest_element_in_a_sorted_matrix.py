# kth-smallest-element-in-a-sorted-matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

'''

# Approach 1: using binary search
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    m = len(matrix[0])

    def countLessThanEqual(value):
        count = 0
        col = m-1

        for row in range(n):
            while(col >=0 and matrix[row][col] > value):
                col-=1
            count+= col+1
        return count


    low = matrix[0][0]
    high = matrix[n-1][m-1]
    res = -1

    while(low<=high):
        mid = low+(high-low)//2

        if(countLessThanEqual(mid) >=k):
            res = mid
            high = mid-1
        else:
            low = mid+1
    return res