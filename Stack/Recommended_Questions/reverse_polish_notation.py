# evaluate-reverse-polish-notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

'''

def evalRPN(tokens: List[str]) -> int:
    st = []
    for value in tokens:
        if value in ['*',"-","+","/"]:
            op2 = st.pop()
            op1 = st.pop()
            result = 0
            if value == "*":
                result = op1*op2
            elif value == "-":
                result = op1-op2
            elif value == "+":
                result = op1+op2
            else:
                result = int(op1/op2)
            st.append(result)
        else:
            st.append(int(value))
    return st[0]