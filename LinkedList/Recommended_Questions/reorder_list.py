# reorder-list
# https://leetcode.com/problems/reorder-list/description/
'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

'''

# Approach 1: split the LL into equal at middle and reverse the second part and attact curr element
def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    first = head
    second = head
    while(second.next and second.next.next):
        first = first.next
        second = second.next.next
        
    prev,curr = None,first.next
    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    first.next = None
    
    head1 = head
    head2 = prev
    while(head2):
        temp1 = head1.next
        head1.next = head2
        head1 = head2
        head2 = temp1