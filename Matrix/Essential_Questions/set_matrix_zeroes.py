# set-matrix-zeroes
# https://leetcode.com/problems/set-matrix-zeroes/description/
'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

# Approach: mark row and col where zero is present and then make cell zero where row or col matching
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    row = set([])
    col = set([])
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
    
    for i in range(m):
        for j in range(n):
            if i in row or j in col:
                matrix[i][j] = 0


# Approach 2: InPlace without extra memory instead of the storing row and col in seperate list we can treat matrix 1st row and col to track zeros
def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    col = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        if matrix[i][0] == 0:
            col = 1
        for j in range(1,m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(n-1,-1,-1):
        for j in range(m-1,0,-1):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
        if col:
            matrix[i][0] = 0

    return matrix