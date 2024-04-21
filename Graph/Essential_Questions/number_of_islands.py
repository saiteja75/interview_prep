# number-of-islands
# https://leetcode.com/problems/number-of-islands/description/
'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

# Python Code

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        islands = 0  # Initialize the count of islands
        visit = set()  # Set to keep track of visited cells
        rows, cols = len(grid), len(grid[0])  # Get the number of rows and columns

        # Define a depth-first search (DFS) function
        def dfs(r, c):
            # Check for out-of-bounds, water, or already visited cells
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))  # Mark the current cell as visited
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # Possible directions (up, down, left, right)
            
            # Explore neighbors using DFS
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell contains land and has not been visited
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1  # Increment the island count
                    dfs(r, c)  # Explore the island using DFS

        return islands  # Return the total number of islands