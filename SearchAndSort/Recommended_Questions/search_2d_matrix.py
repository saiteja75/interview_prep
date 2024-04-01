# search-a-2d-matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/
'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

'''

# Approach 1: binary search on matrix
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    low = 0
    high = (m*n)-1

    while(low<=high):
        mid = low+(high-low)//2
        value = matrix[mid//n][mid%n]
        
        if(value == target):
            return True
        elif(value > target):
            high=mid-1
        else:
            low = mid+1
    return False

# Approach 2: two binary searches one for row other for column
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    
    top = 0
    bot = len(matrix) - 1

    while top <= bot:
        mid = (top + bot) // 2

        if matrix[mid][0] < target and matrix[mid][-1] > target:
            break
        elif matrix[mid][0] > target:
            bot = mid - 1
        else:
            top = mid + 1
    
    row = (top + bot) // 2

    left = 0
    right = len(matrix[row]) - 1

    while left <= right:
        mid = (left + right) // 2

        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False