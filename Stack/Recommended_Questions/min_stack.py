# min-stack
# https://leetcode.com/problems/min-stack/description/
'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

'''

class MinStack:

    def __init__(self):
        self.st = []
        self.top1 = -1
        self.currMin = float('inf')
        

    def push(self, val: int) -> None:
        self.currMin = min(self.currMin,val)
        self.st.append([val,self.currMin])
        self.top1+=1

        

    def pop(self) -> None:
        if self.top1 != -1:
            self.st.pop()
            self.top1-=1
            if self.top1 == -1:
                self.currMin = float('inf')
            else:
                self.currMin = self.st[self.top1][1]
        

    def top(self) -> int:
        print(self.top1)
        return self.st[self.top1][0]
        

    def getMin(self) -> int:
        return self.currMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()