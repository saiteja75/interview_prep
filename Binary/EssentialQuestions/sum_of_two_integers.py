# sum-of-two-integers
# https://leetcode.com/problems/sum-of-two-integers/
'''
Given two integers a and b, return the sum of the two integers without using the operators + and -.

'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitShort = 0xffffffff 
        while b & bitShort != 0:
            carry = (a&b)<<1
            a = a^b
            b = carry
        return a & bitShort if b>0 else a
        