# flood-fill
# https://leetcode.com/problems/flood-fill/description/
'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        def dfs(row,col,color,curr):
            if row>=m or col>=n or row<0 or col<0:
                return
            if image[row][col] == curr and image[row][col] !=color:
                image[row][col] = color

                dfs(row-1,col,color,curr)
                dfs(row+1,col,color,curr)
                dfs(row,col-1,color,curr)
                dfs(row,col+1,color,curr)
        dfs(sr,sc,color,image[sr][sc])
        return image        