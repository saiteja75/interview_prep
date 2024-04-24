# pacific-atlantic-water-flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = []
        altantic = []
        for i in range(m):
            pacific.append([i,0])
        for i in range(n):
            pacific.append([0,i])
        for i in range(m):
            altantic.append([i,n-1])
        for i in range(n):
            altantic.append([m-1,i])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(oceans):
            qu = deque(oceans)
            visited = set([])
            while qu:
                row,col = qu.popleft()
                visited.add((row,col))

                for dx,dy in directions:
                    nx,ny = row+dx,col+dy
                    if 0<=nx<m and 0<=ny<n and (nx,ny) not in visited:
                        if heights[nx][ny]>=heights[row][col]:
                            qu.append((nx,ny))
            return visited
        p = bfs(pacific) 
        a = bfs(altantic)
        return p.intersection(a)
        