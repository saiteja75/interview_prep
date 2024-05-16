# reverse-bits
# https://leetcode.com/problems/reverse-bits/description/
'''
Reverse bits of a given 32 bits unsigned integer.

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.

'''

class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
        