# rotting-oranges
# https://leetcode.com/problems/rotting-oranges/description/
'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        miniTime = 0
        m = len(grid)
        n = len(grid[0])
        qu = deque([])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    qu.append([(i,j),0])
        while qu:
            cell,count = qu.popleft()
            x,y = cell
            miniTime = max(miniTime,count)

            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        qu.append([(nx,ny),count+1])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return miniTime