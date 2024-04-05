# remove-nth-node-from-end-of-list
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

'''

# Approach 1: two Pointer
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    first = head
    second = head
    i = 0
    while(i<n):
        first = first.next
        i+=1
    
    if(first == None):
        return head.next

    while(first.next):
        first = first.next
        second = second.next
    
    second.next = second.next.next

    return head
        