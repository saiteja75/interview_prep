# counting-bits
# https://leetcode.com/problems/counting-bits/description/
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

'''

# Approach 1:
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            while i:
                count+= i&1
                i=i>>1
            res.append(count)
        return res

# Approach 2:
class Solution:
    def returnResult(self,i, n, ans):
        if(i==n):
            return ans
        ans[i] = ans[i//2]+i%2
        return self.returnResult(i+1,n,ans)
    def countBits(self, n: int) -> List[int]:
        result = [0]*(n+1)
        return self.returnResult(1,n+1,result)
                