# implement-queue-using-stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/
'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
'''

class MyQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:
        self.st1.append(x)

    def pop(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

    def peek(self) -> int:
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2[-1]

    def empty(self) -> bool:
        return not self.st1 and not self.st2
    


class MyQueue:

    def __init__(self):
        self.stack = []
        self.top = -1
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.top+=1
        
    def pop(self) -> int:
        self.stack = self.stack[::-1]
        value = self.stack.pop()
        self.top-=1
        self.stack = self.stack[::-1]
        return value
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if self.top == -1:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()