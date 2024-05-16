# number of visible people in a queue
# LeetCode Problem Link: https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/
'''
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.
'''

# Approach: using monotonic stack and start from right
def canSeePersonsCount(heights: List[int]) -> List[int]:
    # length of the heights
    n = len(heights)
    # stack to main the monotonic stack to track the next greater element
    stack = []
    # final result
    ans = [0] * n

    # iterate from the end
    for i in range(n - 1, -1, -1):
        # count the peoples heights less than current height
        cur = 0

        # count the people who are less than current person height
        # if they are any remove it from stack to maintain monotonic in nature
        while stack and stack[-1] < heights[i]:
            # if current height is greated than in stack top remove it(which contain heights of people in right of queue)
            stack.pop()
            # increment the count
            cur += 1

        # After the iteration add the count and
        # if the stack is empty we have no person bigger than current person
        # if the stack is not empty that mean a person height is higher than current person
        # so we need to add that higher person count as current person can first higher person
        ans[i] = cur + int(len(stack) > 0)
        # add it into the stack
        stack.append(heights[i])

    # return result
    return ans