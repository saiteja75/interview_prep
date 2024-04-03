# valid-sudoku
# https://leetcode.com/problems/valid-sudoku/
'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''

# Approach 1: maintaining set for each row and col and for sub matrix
def isValidSudoku(board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        block = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                curr = board[i][j]
                if curr == '.':
                    continue
                print(block[i // 3][j // 3])
                if (curr in rows[i]) or (curr in cols[j]) or (curr in block[i // 3][j // 3]):
                    return False
                rows[i].add(curr)
                cols[j].add(curr)
                block[i // 3][j // 3].add(curr)
        return True