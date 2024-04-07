# stack-using-queues
# https://leetcode.com/problems/implement-stack-using-queues/description/
'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
'''

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


class MyStack:

    def __init__(self):
        self.queue = []
        self.top1 = -1

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.top1+=1
        

    def pop(self) -> int:
        self.queue = self.queue[::-1]
        value = self.queue.pop(0)
        self.queue = self.queue[::-1]
        self.top1-=1
        return value

        

    def top(self) -> int:
        return self.queue[self.top1]
        

    def empty(self) -> bool:
        if self.top1 == -1:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()