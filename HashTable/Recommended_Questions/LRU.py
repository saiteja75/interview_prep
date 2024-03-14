# least recently used
# leetcode problem link:  https://leetcode.com/problems/lru-cache/description/
'''
Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
'''

# Approach 1: using hashMap and stack (array)
class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.hashMap = {}
        self.store = []
    
    def updateStore(self, key):
        exists = self.hashMap.get(key,None)
        if exists == None:
            self.store.append(key)
        else:
            self.store.remove(key)
            self.store.append(key)

    def getLeastUsed(self):
        return self.store.pop(0)
        

    def get(self, key: int) -> int:
        if(self.hashMap.get(key,-1) == -1):
            return -1
        self.updateStore(key)
        return self.hashMap[key]
        

    def put(self, key: int, value: int) -> None:
        if(self.size <= len(self.store) and self.hashMap.get(key,-1) == -1):
            leastUsed = self.getLeastUsed()
            self.hashMap.pop(leastUsed,None)
        self.updateStore(key)
        self.hashMap[key] = value
            

        
# Approach 2: using hashMap and DLL
class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addNode(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    def deleteNode(self, delnode):
        prevv = delnode.prev
        nextt = delnode.next
        prevv.next = nextt
        nextt.prev = prevv

    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            del self.m[key]
            self.deleteNode(curr)

        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)

        self.addNode(self.Node(key, value))
        self.m[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)