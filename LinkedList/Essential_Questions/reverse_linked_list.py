# reverse-linked-list
# https://leetcode.com/problems/reverse-linked-list/description/
'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None

    while(curr!=None):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev