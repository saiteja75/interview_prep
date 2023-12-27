# range sum query 2d
# Leet Code Problem: https://leetcode.com/problems/range-sum-query-2d-immutable/description/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = []
        # precomputing in till that index
        for i in range(len(matrix)):
            currSum = []
            total = 0
            for j in range(len(matrix[0])):
                total+=matrix[i][j]
                currSum.append(total)
            self.preSum.append(currSum)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        # iterating each row and compute the total till that col2 and subtract col1-1
        for i in range(row1,row2+1):
            if col1 > 0:
                total+= self.preSum[i][col2]-self.preSum[i][col1-1]
            else:
                total+= self.preSum[i][col2]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
    

# Approach 2: with O(1) time complexity
# Answer Link: https://leetcode.com/problems/range-sum-query-2d-immutable/solutions/572648/c-java-python-prefix-sum-with-picture-explain-clean-concise/
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * (n + 1) for _ in range(m + 1)]  # sum[i][j] is sum of all elements inside the rectangle [0,0,i,j]
        for r in range(1, m + 1):
            for c in range(1, n + 1):
                self.sum[r][c] = self.sum[r - 1][c] + self.sum[r][c - 1] - self.sum[r - 1][c - 1] + matrix[r - 1][c - 1]

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1  # Since our `sum` starts by 1 so we need to increase r1, c1, r2, c2 by 1
        return self.sum[r2][c2] - self.sum[r2][c1 - 1] - self.sum[r1 - 1][c2] + self.sum[r1 - 1][c1 - 1]
Java