# container with most water
# leet code problem: https://leetcode.com/problems/container-with-most-water/description/
'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''


# Approach: figuring out least two pointers a container can be formed to form max area
def maxArea(height: List[int]) -> int:
    # length of the height
    n = len(height)
    # left to point the starting point of the container
    left = 0
    # right to point the end point of the container
    right = n-1
    # to store the max area
    maxArea = float('-inf')

    # two pointers start from big container and keep on decreasing to form max area
    while(left<right):
        # area of the rectangle is x axis and y axis
        # x axis: right-left
        # y axis: minimum height of y axis since least height can fill the container not the higher height
        currArea = (right-left)*min(height[left],height[right])
        # update the max area
        maxArea = max(maxArea,currArea)
        # try to shift the left or right based on max height
        if height[left]<=height[right]:
            left+=1
        else:
            right-=1
    
    # return maxArea
    return maxArea