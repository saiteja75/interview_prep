# 01-matrix
# https://leetcode.com/problems/01-matrix/description/
'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

'''

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        qu = deque([])
        for  i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    qu.append([i,j])
        
        while qu:
            x,y = qu.popleft()

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    if distance[nx][ny] > distance[x][y]+1:
                        distance[nx][ny] = distance[x][y]+1
                        qu.append([nx,ny])
        return distance


        