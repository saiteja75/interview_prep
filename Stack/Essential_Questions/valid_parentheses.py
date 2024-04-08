# valid-parentheses
# https://leetcode.com/problems/valid-parentheses/description/
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
def isValid(s: str) -> bool:
    st = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        elif len(st) and ((s[i] == ')' and st[-1] == '(') or (s[i] == '}' and st[-1] == '{') or (s[i] == ']' and st[-1] == '[')):
            st.pop()
        else:
            return False
        
    if len(st):
        return False
    return True