# letter-combinations-of-a-phone-number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

'''

# Approach: Recursion backtracking
def letterCombinations(digits: str) -> List[str]:
    if(digits == ""):
        return []
    res = []
    hashMap = {
        "2": ['a','b','c'],
        "3": ['d','e','f'],
        "4": ['g','h','i'],
        "5": ['j','k','l'],
        "6": ['m','n','o'],
        "7": [ 'p','q','r', 's'],
        "8": ['t','u','v'],
        "9": ['w','x','y','z']
    }
    def compute(index,s,digits,res,hashMap):
        if (index == len(digits)):
            res.append("".join(s[:]))
            return
        for i in hashMap[digits[index]]:
            s.append(i)
            compute(index+1,s,digits,res,hashMap)
            s.pop()
    compute(0,[],digits,res,hashMap)
    return res