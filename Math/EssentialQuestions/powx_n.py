# powx-n
# https://leetcode.com/problems/powx-n/description/
'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        sign = 1
        if n<0:
            sign = -1
            n = -1*n

        while(n>0):
            if n%2 == 0:
                x=x*x
                n=n//2
            else:
                res*=x
                n-=1
        
        if sign < 0:
            return 1/res
        return res
            