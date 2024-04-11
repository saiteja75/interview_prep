# basic-calculator-ii
# https://leetcode.com/problems/basic-calculator-ii/description/
'''
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

'''

# Approach 1: PostFix and Evaluate the postfix
def calculate(s: str) -> int:
    def prec(op):
        if op == '*' or op == '/':
            return 2
        elif op == '-' or op == '+':
            return 1
        else:
            return -1

    post = []
    res = []
    st = []
    s1 = ''
    for i in s:
        if i in ['+','-','*','/']:
            if s1:
                post.append(int(s1))
                s1=''
            while(st and prec(st[-1])>=prec(i)):
                post.append(st.pop())
            st.append(i)
        else:
            s1+=i
    if s1:
        post.append(int(s1))
    while(st):
        post.append(st.pop())
    
    for i in post:
        if i in ['-','+','*','/']:
            op2= res.pop()
            op1 = res.pop()
            if i == '-':
                res.append(op1-op2)
            elif i == '+':
                res.append(op1+op2)
            elif i == '*':
                res.append(op1*op2)
            else:
                res.append(int(op1/op2))
        else:
            res.append(i)

    return res[-1]


# Approach 2: Stack and recursion
def calculate(s):    
    def calc(it):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(int(stack.pop() / v))
    
        num, stack, sign = 0, [], "+"
        
        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":
                num, j = calc(it + 1)
                it = j - 1
            elif s[it] == ")":
                update(sign, num)
                return sum(stack), it + 1
            it += 1
        update(sign, num)
        return sum(stack)

    return calc(0)