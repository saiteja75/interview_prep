# Sort Colors
# Leetcode Problem Link: https://leetcode.com/problems/sort-colors/description/
'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
'''

def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Creating Three pointers to track 3 different colors i.e numbers
        # left -> 0 (after iteration left points to end of the number 0)
        # middle -> 1 (after iteration middle points to end of the number 1)
        # right -> 2 (after iteration right points to start of number 2)
        left,middle,right = 0,0,len(nums)-1

        # Iterate middle till the right pointer
        while(middle<=right):
            # if the number is 0 this should always be at the begin so
            # swap the number to the left and increment left and middle
            if nums[middle] == 0:
                nums[left],nums[middle] = nums[middle],nums[left]
                left+=1
                middle+=1
            # if the number is 1 it will be on the middle so increment middle
            elif nums[middle] == 1:
                middle+=1
            # if the number is 2 this should be always be at the end so
            # swap the number with right and decrement the right since one number 2 is reached it correct position
            # DO NOT INCREMENT MIDDLE SINCE THE NUMBER AT RIGHT IS STILL NOT PROCESSED (IT CAN ANY OF THE VALUE) 
            else:
                nums[right],nums[middle] = nums[middle],nums[right]
                right-=1