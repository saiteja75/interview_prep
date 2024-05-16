# number-of-1-bits
# https://leetcode.com/problems/number-of-1-bits/description/
'''
Write a function that takes the binary representation of a positive integer and returns the number of 
set bits it has (also known as the Hamming weight).

'''
# Approach 1: check the number modulo 2 is not zero
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n%2:
                count+=1
            n = n//2
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        c =0
        while(n):
            if (n&1):
                c+=1
            n = n>>1
        return c   

# Approach 2: recursion
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Base case: if n is 0, return 0 as there are no set bits
        if n == 0:
            return 0
        
        # Use bitwise AND with 1 to check the least significant bit
        # Add it to the count and recursively call the function with right shift by 1
        return (n & 1) + self.hammingWeight(n >> 1)
