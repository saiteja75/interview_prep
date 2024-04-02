# spiral-matrix
# https://leetcode.com/problems/spiral-matrix/description/
'''
Given an m x n matrix, return all elements of the matrix in spiral order.

'''

# Approach 1: tracking the boundaries left right top bottom
def spiralOrder(matrix: List[List[int]]) -> List[int]:
    m = len(matrix)
    n = len(matrix[0])
    left = top = 0
    right = n-1
    bottom = m-1
    res = []

    while(left<=right and top<=bottom):
        for i in range(left,right+1):
            res.append(matrix[top][i])
        top+=1
        for j in range(top,bottom+1):
            res.append(matrix[j][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                res.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for j in range(bottom,top-1,-1):
                res.append(matrix[j][left])
            left+=1
    return res