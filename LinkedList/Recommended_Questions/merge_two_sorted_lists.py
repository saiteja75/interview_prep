# merge-two-sorted-lists
# https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

# Approach 1: use dummy head node
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    curr = ListNode(-1)
    res = curr
    curr1 = list1
    curr2 = list2

    while(curr1 and curr2):
        if(curr1.val<curr2.val):
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        curr = curr.next
    
    while(curr1):
        curr.next = curr1
        curr1 = curr1.next
        curr = curr.next

    while(curr2):
        curr.next = curr2
        curr2 = curr2.next   
        curr = curr.next

    return res.next