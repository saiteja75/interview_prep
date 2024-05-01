# merge-k-sorted-lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/
'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
'''

# Approach 1: Heap
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i,node in enumerate(lists):
            if node:
                hq.heappush(heap,(node.val,i,node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            _,index,node = hq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                hq.heappush(heap,(node.next.val,index,node.next))
        return dummy.next

        