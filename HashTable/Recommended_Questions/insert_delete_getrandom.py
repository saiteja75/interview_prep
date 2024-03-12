# insert delete getrandom o1
# leetcode problem link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/
'''
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.
'''
import random
class RandomizedSet:

    def __init__(self):
        self.hashMap = {}

        

    def insert(self, val: int) -> bool:
        if self.hashMap.get(val,None) == None:
            self.hashMap[val] = True
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.hashMap.get(val,None) == None:
            return False
        del self.hashMap[val]
        return True
        

    def getRandom(self) -> int:
        keys = list(self.hashMap.keys())
        return keys[random.randrange(len(keys))]        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()