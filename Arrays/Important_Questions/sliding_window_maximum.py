# sliding window maximum
# leet code problem: https://leetcode.com/problems/sliding-window-maximum/submissions/

from collections import deque


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    # res is for result to be returned
    res = []
    # two pointers for sliding window
    left = right = 0
    # deque i.e double ended queue where you push and pop from front and back of the deque
    # In this case we are using store indexes in decensding order and once k subarray is formed take the first element
    q = deque()

    # iterating using the right pointer
    while right < len(nums):
        # check if the deque is not empty and if incoming element is greater than rear index value remove it
        # as we are only maintaining indexes based on its value in descending order
        while q and nums[right] > nums[q[-1]]:
            q.pop()
        # appending the right element on this correct positing to maintain descending order
        q.append(right)

        # check if deque left most element is not in current window remove it from the deque
        if left > q[0]:
            q.popleft()
        
        # if the window size is reached to k or greater than k
        # max element in window would be deque front element as we are maintiaining in descending order
        if right + 1 >= k:
            res.append(nums[q[0]])
            # moving the left for next window
            left += 1
        # move the right index to maintain k window subarray
        right += 1
    # return result
    return res