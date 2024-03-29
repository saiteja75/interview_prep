# generate-parentheses
# https://leetcode.com/problems/generate-parentheses/description/
'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''


def generateParenthesis(n: int) -> List[str]:
    # result list
    res = []

    # helper function to get valid parenthesis
    def dfs(s,open,close,res):
        # if all open and close variables are completed we found the solution add it result
        if(open == 0 and close == 0):
            res.append(s)
            return
        # if the close brackets are completed or open is close 
        elif(close == 0 or open == close):
            # then we need start with open brackets
            dfs(s+'(',open-1,close,res)
        # if the open brackets are completed
        elif(open == 0):
            # use all remaining close brackets
            dfs(s+')',open,close-1,res)
        # else try both combinations
        else:
            # with open brackets
            dfs(s+'(',open-1,close,res)
            # with close brackets
            dfs(s+')',open,close-1,res)
    dfs('',n,n,res)
    return res
        