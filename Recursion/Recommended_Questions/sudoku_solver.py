# sudoku-solver
# https://leetcode.com/problems/sudoku-solver/description/
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
'''


# Approach 1: recursion and backtracking
def solveSudoku(board: List[List[str]]) -> None:
    n = 9
    
    
    def isValid(row, col, ch):
        row, col = int(row), int(col)
        
        for i in range(9):
            
            if board[i][col] == ch:
                return False
            if board[row][i] == ch:
                return False
            
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                return False
        
        return True
        
    def solve(row, col):
        if row == n:
            return True
        if col == n:
            return solve(row+1, 0)
        
        if board[row][col] == ".":
            for i in range(1, 10):
                if isValid(row, col, str(i)):
                    board[row][col] = str(i)
                    
                    if solve(row, col + 1):
                        return True
                    else:
                        board[row][col] = "."
            return False
        else:
            return solve(row, col + 1)
        
        
    
    solve(0, 0)