# rotate-image
# https://leetcode.com/problems/rotate-image/description/
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

# Approach 1: Transpose and Reverse the matrix 
def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    for i in range(n):
        for j in range(n//2):
            matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]