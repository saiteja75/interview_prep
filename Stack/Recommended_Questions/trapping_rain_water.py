# trapping-rain-water
# https://leetcode.com/problems/trapping-rain-water/description/
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

'''

# Approach 1: Monotonic decreasing stack:
def trap(h: List[int]) -> int:
    res, stack = 0, []
    
    for r, rightBound in enumerate(h):
        while stack and h[stack[-1]] < rightBound:
            bar = h[stack.pop()]
            if stack:
                l, leftBound = stack[-1], h[stack[-1]]
                minBound = min(rightBound, leftBound)
                res += (r - l - 1) * (minBound - bar)
        stack.append(r)
    
    return res


# Approach 2: Two Pointer
def trap(height: List[int]) -> int:
    leftMax = []
    currMax = float('-inf')
    for i in height:
        currMax = max(currMax,i)
        leftMax.append(currMax)

    rightMax = []
    currMax = float('-inf')
    for i in height[::-1]:
        currMax = max(currMax,i)
        rightMax.append(currMax)
    rightMax.reverse()
    
    res = 0
    for i in range(len(height)):
        res+=min(leftMax[i],rightMax[i])-height[i]
    return res