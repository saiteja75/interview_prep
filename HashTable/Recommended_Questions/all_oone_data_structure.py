# all-oone-data-structure
# Leet Code Problem Link: https://leetcode.com/problems/all-oone-data-structure/description/
'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.
'''

# Approach:hashMap and Double linked list
# reference: https://leetcode.com/problems/all-oone-data-structure/solutions/4667945/doubly-linked-list/s
class LinkedList:
    def __init__(self, val, cnt=0, next=None, prev=None):
        self.val = val
        self.cnt = cnt
        self.next = next
        self.prev = prev

class AllOne:

    def __init__(self):
        self.head = LinkedList(val='')
        self.tail = LinkedList(val='', cnt=float('inf'), prev=self.head)
        self.head.next = self.tail
        self.dict = {}

    def swap_nodes(self, node1, node2, node3, node4):
        node1.next = node3
        node3.prev, node3.next = node1, node2
        node2.prev, node2.next = node3, node4
        node4.prev = node2
        return (node1, node3, node2, node4)

    def inc(self, key: str) -> None:
        if key not in self.dict:
            prev, curr = self.head, self.head.next
            node = LinkedList(val=key, cnt=1, next=curr, prev=prev)
            prev.next = node
            curr.prev = node
            self.dict[key] = node
            return 

        node = self.dict[key]
        node.cnt += 1   

        while node.next.cnt < node.cnt: # swap nodes
            node1, node2, node, node4 = self.swap_nodes(node.prev, node, node.next, node.next.next)
            self.dict[key] = node

    def dec(self, key: str) -> None:
        node = self.dict[key]
        node.cnt -= 1
        if node.cnt == 0:
            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev
            del self.dict[key]
            return
        while node.prev.cnt > node.cnt: # swap nodes
            node1, node, node3, node4 = self.swap_nodes(node.prev.prev, node.prev, node, node.next)
            self.dict[key] = node

    def getMaxKey(self) -> str:
        if self.tail.prev:
            return self.tail.prev.val
        return ''

    def getMinKey(self) -> str:    
        if self.head.next:
            return self.head.next.val
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()