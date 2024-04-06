# merge-k-sorted-lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

'''

# Merge Sort
class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        while left:
            temp.next = left
            temp = temp.next
            left = left.next
        while right:
            temp.next = right
            temp = temp.next
            right = right.next
        return dummy.next
    
    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)
    


# Brute Force
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return
        if n == 1:
            return lists[0]
        head = lists[0]
        tail = head
        while(tail and tail.next):
            tail = tail.next
        i = 1
        while(i<n):
            curr = lists[i]
            while(curr):
                temp = curr.next
                if head == None:
                    head = curr
                    tail = head
                    while(tail and tail.next):
                        tail = tail.next
                    break
                elif curr.val >= tail.val:
                    tail.next = curr
                    tail = tail.next
                elif curr.val < head.val:
                    temp1 = head
                    curr.next = temp1
                    head = curr
                else:
                    mainHead = head
                    prev = mainHead
                    while(mainHead and mainHead.val < curr.val):
                        prev = mainHead
                        mainHead = mainHead.next
                    temp1 = prev.next
                    prev.next = curr
                    curr.next = temp1
                curr = temp
            i+=1
        return head

        

